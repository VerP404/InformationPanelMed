from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
import pandas as pd
import io
from .models import RegisteredPatients, Page, Building, Specialty, Organization
from .forms import UploadDataForm
from django.contrib import messages


def index(request):
    organization = Organization.objects.first()
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    pages = Page.objects.all()
    context = {
        'report_datetime': report_datetime,
        'pages': pages,
        'organization': organization,
    }
    return render(request, 'index.html', context)


def get_report_datetime(request):
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    return JsonResponse({'report_datetime': report_datetime})


def dynamic_page(request, path):
    organization = Organization.objects.first()
    page = get_object_or_404(Page, path=path)
    data_from_db = RegisteredPatients.objects.filter(subdivision=page.subdivision)
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'page': page,
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': f'/get_data_{path}/',
        'organization': organization,
    }
    return render(request, 'peopledash/base_peopledash.html', context)


def dynamic_page_get_data(request, path):
    page = get_object_or_404(Page, path=path)
    data_from_db = RegisteredPatients.objects.filter(subdivision=page.subdivision)
    data = []
    for row in data_from_db:
        data.append({
            'Наименование должности': row.speciality,
            'Всего_1': row.slots_today,
            'Слоты свободные для записи_1': row.free_slots_today,
            'Слоты свободные для записи_14': row.free_slots_14_days,
        })
    return JsonResponse(data, safe=False)


def process_transformer_files(df_1, df_14, report_dt):
    specialties = list(Specialty.objects.values_list('name', flat=True))
    organizations = list(Organization.objects.values_list('name', flat=True))
    corpus_mapping = {}
    for page in Page.objects.all():
        filters = list(page.building.subdivisions.values_list('name', flat=True))
        corpus_mapping[page.subdivision] = filters

    def update_df(df):
        filtered_dfs = []
        for corpus, filters in corpus_mapping.items():
            filtered_df = df[
                (df['Наименование МО'].isin(organizations)) &
                (df['Тип приёма'] == 'Первичный прием') &
                (df['Обособленное подразделение'].isin(filters)) &
                (df['Наименование должности'].isin(specialties))
                ].copy()
            if filtered_df.empty:
                print(f"No data found for corpus {corpus} with filters {filters}.")
            else:
                filtered_df['Обособленное подразделение'] = corpus
                filtered_dfs.append(filtered_df)

        if not filtered_dfs:  # If no data is found
            return pd.DataFrame()  # Return an empty DataFrame to avoid errors

        combined_df = pd.concat(filtered_dfs)

        combined_df['Всего'] = pd.to_numeric(combined_df['Всего'], errors='coerce')
        combined_df['Слоты свободные для записи'] = pd.to_numeric(combined_df['Слоты свободные для записи'],
                                                                  errors='coerce')

        grouped_df = combined_df.groupby(['Обособленное подразделение', 'Наименование должности']).agg({
            'Всего': 'sum',
            'Слоты свободные для записи': 'sum'
        })
        # grouped_df = grouped_df.reset_index()

        return grouped_df

    def union_df(gr_1, gr_14):
        if gr_1.empty and gr_14.empty:
            return pd.DataFrame()

        merged_df = pd.merge(gr_14, gr_1, on=['Обособленное подразделение', 'Наименование должности'], how='outer',
                             suffixes=('_14', '_1'))
        merged_df[['Всего_14', 'Слоты свободные для записи_14', 'Всего_1', 'Слоты свободные для записи_1']] = merged_df[
            ['Всего_14', 'Слоты свободные для записи_14', 'Всего_1', 'Слоты свободные для записи_1']
        ].fillna(0)
        merged_df['Всего_1'] = merged_df['Всего_1'].astype(int)
        merged_df['Слоты свободные для записи_1'] = merged_df['Слоты свободные для записи_1'].astype(int)
        merged_df['Дата и время обновления'] = report_dt.strftime('%H:%M %d.%m.%Y')
        return merged_df

    def save_registered_patients_from_dataframe(df):
        RegisteredPatients.objects.all().delete()
        for index, row in df.iterrows():
            RegisteredPatients.objects.create(
                subdivision=row['Обособленное подразделение'],
                speciality=row['Наименование должности'],
                slots_today=row['Всего_1'],
                free_slots_today=row['Слоты свободные для записи_1'],
                slots_14_days=row['Всего_14'],
                free_slots_14_days=row['Слоты свободные для записи_14'],
                report_datetime=row['Дата и время обновления']
            )

    data = union_df(update_df(df_1), update_df(df_14))
    if not data.empty:
        save_registered_patients_from_dataframe(data)
    else:
        print("Нет данных для сохранения.")  # Добавим отладочное сообщение


def upload_data(request):
    organization = Organization.objects.first()

    if request.method == 'POST':
        form = UploadDataForm(request.POST, request.FILES)
        if form.is_valid():
            file_today = request.FILES['file_today']
            file_buffer = io.BytesIO(file_today.read())
            df_1 = pd.read_csv(file_buffer, encoding='cp1251', delimiter=';')

            file_14_days = request.FILES['file_14_days']
            file_buffer = io.BytesIO(file_14_days.read())
            df_14 = pd.read_csv(file_buffer, encoding='cp1251', delimiter=';')

            report_datetime = form.cleaned_data['report_datetime']

            process_transformer_files(df_1, df_14, report_datetime)

            messages.success(request, 'Данные успешно сохранены')

            return redirect(request.META.get('HTTP_REFERER', 'upload_data'))

    else:
        form = UploadDataForm()

    return render(request, 'peopledash/upload_data.html', {
        'form': form,
        'organization': organization
    })
