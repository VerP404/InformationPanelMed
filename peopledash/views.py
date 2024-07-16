from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import pandas as pd
import io
from .models import RegisteredPatients
from peopledash.forms import UploadDataForm
from django.contrib import messages


def index(request):
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'report_datetime': report_datetime,
    }
    return render(request, 'index.html', context)


def get_report_datetime(request):
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    return JsonResponse({'report_datetime': report_datetime})


def korpus_1(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Поликлиника")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_k1/',
    }
    return render(request, 'peopledash/korpus_1.html', context)


def korpus_1_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Поликлиника")
    data = []
    for row in data_from_db:
        data.append({
            'Наименование должности': row.speciality,
            'Всего_1': row.slots_today,
            'Слоты свободные для записи_1': row.free_slots_today,
            'Слоты свободные для записи_14': row.free_slots_14_days,
        })
    return JsonResponse(data, safe=False)


def korpus_2(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Детская поликлиника")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_k2/',

    }
    return render(request, 'peopledash/korpus_2.html', context)


def korpus_2_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Детская поликлиника")
    data = []
    for row in data_from_db:
        data.append({
            'Наименование должности': row.speciality,
            'Всего_1': row.slots_today,
            'Слоты свободные для записи_1': row.free_slots_today,
            'Слоты свободные для записи_14': row.free_slots_14_days,
        })
    return JsonResponse(data, safe=False)


def korpus_3(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Яменская врачебная амбулатория")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_k3/',

    }
    return render(request, 'peopledash/korpus_3.html', context)


def korpus_3_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Яменская врачебная амбулатория")
    data = []
    for row in data_from_db:
        data.append({
            'Наименование должности': row.speciality,
            'Всего_1': row.slots_today,
            'Слоты свободные для записи_1': row.free_slots_today,
            'Слоты свободные для записи_14': row.free_slots_14_days,
        })
    return JsonResponse(data, safe=False)


def korpus_6(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Новоживотинновская участковая больница")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_k6/',

    }
    return render(request, 'peopledash/korpus_6.html', context)


def korpus_6_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Новоживотинновская участковая больница")
    data = []
    for row in data_from_db:
        data.append({
            'Наименование должности': row.speciality,
            'Всего_1': row.slots_today,
            'Слоты свободные для записи_1': row.free_slots_today,
            'Слоты свободные для записи_14': row.free_slots_14_days,
        })
    return JsonResponse(data, safe=False)


def korpus_dp1(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Березовский ФАП")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_dp1/',

    }
    return render(request, 'peopledash/korpus_dp1.html', context)


def korpus_dp1_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Березовский ФАП")
    data = []
    for row in data_from_db:
        data.append({
            'Наименование должности': row.speciality,
            'Всего_1': row.slots_today,
            'Слоты свободные для записи_1': row.free_slots_today,
            'Слоты свободные для записи_14': row.free_slots_14_days,
        })
    return JsonResponse(data, safe=False)


def korpus_dp8(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Центр общей врачебной практики")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_dp8/',

    }
    return render(request, 'peopledash/korpus_dp8.html', context)


def korpus_dp8_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Центр общей врачебной практики")
    data = []
    for row in data_from_db:
        data.append({
            'Наименование должности': row.speciality,
            'Всего_1': row.slots_today,
            'Слоты свободные для записи_1': row.free_slots_today,
            'Слоты свободные для записи_14': row.free_slots_14_days,
        })
    return JsonResponse(data, safe=False)


def korpus_jk(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Женская консультация")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_jk/',

    }
    return render(request, 'peopledash/korpus_jk.html', context)


def korpus_jk_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Женская консультация")
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
    # Список отслеживаемых должностей
    desired_positions = [
        'врач-хирург', 'врач-гериатр',
        'врач-оториноларинголог', 'врач-офтальмолог', 'врач-терапевт участковый',
        'врач общей практики (семейный врач)', 'врач-терапевт', 'врач-акушер-гинеколог',
        'врач-педиатр участковый', 'врач-педиатр',
        'врач - детский хирург'
    ]
    # Словарь соответствия подразделения корпусам
    corpus_mapping = {
        'ПОЛИКЛИНИКА': 'Поликлиника',
        'Детская поликлиника': 'Детская поликлиника',
        'ЯМЕНСКАЯ ВРАЧЕБНАЯ АМБУЛАТОРИЯ': 'Яменская врачебная амбулатория',
        'НОВОЖИВОТИННОВСКАЯ УЧАСТКОВАЯ БОЛЬНИЦА': 'Новоживотинновская участковая больница',
        'ФЕЛЬДШЕРСКО-АКУШЕРСКИЕ ПУНКТЫ, Березовский фельдшерско-акушерский пункт': 'Березовский ФАП',
        'ЦЕНТР ОБЩЕЙ ВРАЧЕБНОЙ ПРАКТИКИ (СЕМЕЙНОЙ МЕДИЦИНЫ)': 'Центр общей врачебной практики',
    }

    def update_df(df):
        filtered_df = df[
            (df['Наименование МО'] == 'БУЗ ВО "Рамонская РБ"') &
            (df['Тип приёма'] == 'Первичный прием') &
            (df['Наименование должности'].isin(desired_positions))
            ]
        filtered_df = filtered_df.copy()
        filtered_df.loc[:, 'Корпус'] = filtered_df['Обособленное подразделение'].map(corpus_mapping)
        # Преобразование текстовых значений в числа для столбцов "Всего" и "Слоты свободные для записи"
        filtered_df['Всего'] = pd.to_numeric(filtered_df['Всего'], errors='coerce')
        filtered_df['Слоты свободные для записи'] = pd.to_numeric(filtered_df['Слоты свободные для записи'],
                                                                  errors='coerce')

        # Группировка и суммирование числовых значений по столбцам "Корпус" и "Наименование должности"
        grouped_df = filtered_df.groupby(['Корпус', 'Наименование должности']).agg({
            'Всего': 'sum',
            'Слоты свободные для записи': 'sum'
        }).reset_index()
        return grouped_df

    def union_df(gr_1, gr_14):
        # Объединение двух файлов по столбцам "Корпус" и "Наименование должности"
        merged_df = pd.merge(gr_14, gr_1, on=['Корпус', 'Наименование должности'], how='outer', suffixes=('_14', '_1'))
        merged_df[['Всего_14', 'Слоты свободные для записи_14', 'Всего_1', 'Слоты свободные для записи_1']] = merged_df[
            ['Всего_14', 'Слоты свободные для записи_14', 'Всего_1', 'Слоты свободные для записи_1']
        ].fillna(0)
        # Преобразование значений в столбцах 'Всего_1' и 'Слоты свободные для записи_1' в целые числа
        merged_df['Всего_1'] = merged_df['Всего_1'].astype(int)
        merged_df['Слоты свободные для записи_1'] = merged_df['Слоты свободные для записи_1'].astype(int)
        merged_df['Дата и время обновления'] = report_dt.strftime('%H:%M %d.%m.%Y')

        return merged_df

    def save_registered_patients_from_dataframe(df):
        RegisteredPatients.objects.all().delete()
        for index, row in df.iterrows():
            RegisteredPatients.objects.create(
                subdivision=row['Корпус'],
                speciality=row['Наименование должности'],
                slots_today=row['Всего_1'],
                free_slots_today=row['Слоты свободные для записи_1'],
                slots_14_days=row['Всего_14'],
                free_slots_14_days=row['Слоты свободные для записи_14'],
                report_datetime=row['Дата и время обновления']
            )

    data = union_df(update_df(df_1), update_df(df_14))
    save_registered_patients_from_dataframe(data)


def upload_data(request):
    if request.method == 'POST':
        form = UploadDataForm(request.POST, request.FILES)
        if form.is_valid():
            # Обработка данных формы
            file_today = request.FILES['file_today']
            file_buffer = io.BytesIO(file_today.read())
            df_1 = pd.read_csv(file_buffer, encoding='cp1251', delimiter=';')

            file_14_days = request.FILES['file_14_days']
            file_buffer = io.BytesIO(file_14_days.read())
            df_14 = pd.read_csv(file_buffer, encoding='cp1251', delimiter=';')

            report_datetime = form.cleaned_data['report_datetime']

            process_transformer_files(df_1, df_14, report_datetime)

            messages.success(request, 'Данные успешно сохранены')  # Уведомление

            return redirect(request.META.get('HTTP_REFERER', 'upload_data'))

    else:
        form = UploadDataForm()

    return render(request, 'peopledash/upload_data.html', {'form': form})
