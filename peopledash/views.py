from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import pandas as pd
import io
from .models import RegisteredPatients, TodayData, FourteenDaysData, Page, Building, Specialty, Organization
from .forms import UploadDataForm
from django.contrib import messages
import datetime


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
    # Получение всех специальностей и организаций
    specialties = list(Specialty.objects.values_list('name', flat=True))
    organizations = list(Organization.objects.values_list('name', flat=True))

    # Маппинг корпуса и фильтров
    corpus_mapping = {}
    for page in Page.objects.all():
        filters = list(page.building.subdivisions.values_list('name', flat=True))
        corpus_mapping[page.subdivision] = filters

    def update_db(model):
        # Фильтрация и агрегация данных
        aggregated_data = model.objects.filter(
            organization__in=organizations,
            reception_type='Первичный прием',
            subdivision__in=corpus_mapping.keys(),
            speciality__in=specialties
        ).values(
            'subdivision',
            'speciality'
        ).annotate(
            total=Sum('total_slots'),
            free_slots=Sum('free_slots')
        )

        return aggregated_data

    def union_data(data_1, data_14):
        # Соединение данных на уровне Python
        result = []
        for item_14 in data_14:
            matching_items = [item for item in data_1 if item['subdivision__building__subdivision'] == item_14[
                'subdivision__building__subdivision'] and item['speciality__name'] == item_14['speciality__name']]
            if matching_items:
                item_1 = matching_items[0]
                result.append({
                    'subdivision': item_14['subdivision__building__subdivision'],
                    'speciality': item_14['speciality__name'],
                    'slots_today': item_1['total'],
                    'free_slots_today': item_1['free_slots'],
                    'slots_14_days': item_14['total'],
                    'free_slots_14_days': item_14['free_slots'],
                    'report_datetime': report_dt
                })
            else:
                result.append({
                    'subdivision': item_14['subdivision__building__subdivision'],
                    'speciality': item_14['speciality__name'],
                    'slots_today': 0,
                    'free_slots_today': 0,
                    'slots_14_days': item_14['total'],
                    'free_slots_14_days': item_14['free_slots'],
                    'report_datetime': report_dt
                })
        return result

    def save_registered_patients(data):
        RegisteredPatients.objects.all().delete()
        RegisteredPatients.objects.bulk_create([RegisteredPatients(**row) for row in data])

    # Обработка данных для сегодня и за 14 дней
    data_1 = update_db(TodayData)
    data_14 = update_db(FourteenDaysData)

    # Объединение данных
    final_data = union_data(data_1, data_14)

    if final_data:
        save_registered_patients(final_data)
    else:
        print("Нет данных для сохранения.")


def upload_data(request):
    if request.method == 'POST':
        form = UploadDataForm(request.POST, request.FILES)
        if form.is_valid():
            file_today = request.FILES['file_today']
            df_1 = pd.read_csv(io.BytesIO(file_today.read()), encoding='cp1251', delimiter=';')

            file_14_days = request.FILES['file_14_days']
            df_14 = pd.read_csv(io.BytesIO(file_14_days.read()), encoding='cp1251', delimiter=';')

            report_datetime = form.cleaned_data['report_datetime']

            process_transformer_files(df_1, df_14, report_datetime)

            messages.success(request, 'Данные успешно сохранены')

            return redirect(request.META.get('HTTP_REFERER', 'upload_data'))
    else:
        form = UploadDataForm()

    return render(request, 'peopledash/upload_data.html', {
        'form': form,
    })
