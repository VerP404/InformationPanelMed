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
    data_from_db = RegisteredPatients.objects.filter(subdivision="Корпус 1")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_k1/',
    }
    return render(request, 'peopledash/korpus_1.html', context)


def korpus_1_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Корпус 1")
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
    data_from_db = RegisteredPatients.objects.filter(subdivision="Корпус 2")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_k2/',

    }
    return render(request, 'peopledash/korpus_2.html', context)


def korpus_2_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Корпус 2")
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
    data_from_db = RegisteredPatients.objects.filter(subdivision="Корпус 3")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_k3/',

    }
    return render(request, 'peopledash/korpus_3.html', context)


def korpus_3_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Корпус 3")
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
    data_from_db = RegisteredPatients.objects.filter(subdivision="Корпус 6")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_k6/',

    }
    return render(request, 'peopledash/korpus_6.html', context)


def korpus_6_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="Корпус 6")
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
    data_from_db = RegisteredPatients.objects.filter(subdivision="ДП 1")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_dp1/',

    }
    return render(request, 'peopledash/korpus_dp1.html', context)


def korpus_dp1_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="ДП 1")
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
    data_from_db = RegisteredPatients.objects.filter(subdivision="ДП 8")
    first_record = RegisteredPatients.objects.first()
    report_datetime = first_record.report_datetime if first_record else None
    context = {
        'data_from_db': data_from_db,
        'report_datetime': report_datetime,
        'url_data': '/get_data_dp8/',

    }
    return render(request, 'peopledash/korpus_dp8.html', context)


def korpus_dp8_get_data(request):
    data_from_db = RegisteredPatients.objects.filter(subdivision="ДП 8")
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
        'Гериатрический кабинет отделения неотложной медицинской помощи 1, корпус 1 пер.Ботанический 47': 'Корпус 1',
        'Городская поликлиника 11, Детская поликлиника 8, Консультативно-диагностическое отделение №1': 'ДП 8',
        'Городская поликлиника 11, Детская поликлиника 8, Консультативно-диагностическое отделение №2': 'ДП 8',
        'Городская поликлиника 11, Детская поликлиника 8, Корпус №7, ул Машиностроителей, 51, Профилактическое отделение': 'ДП 8',
        'Городская поликлиника 11, Детская поликлиника 8, Отделение организации медицинской помощи детям в образовательных организациях, Медицинский персонал по обслуживанию детских садов': 'ДП 8',
        'Городская поликлиника 11, Детская поликлиника 8, Центр охраны зрения детей (корпус №8, ул. Красных Зорь, 36)': 'ДП 8',
        'Городская поликлиника 11, Корпус 3, ул Машиностроителей, 13б': 'Корпус 3',
        'Городская поликлиника 11, Корпус 3, ул Машиностроителей, 13б, Дневной терапевтический стационар': 'Корпус 3',
        'Городская поликлиника 11, Корпус 3, ул Машиностроителей, 13б, Консультативно-диагностическое отделение': 'Корпус 3',
        'Городская поликлиника 11, Корпус 3, ул Машиностроителей, 13б, Отделение общей врачебной практики (семейной медицины) №1': 'Корпус 3',
        'Городская поликлиника 11, Корпус 3, ул Машиностроителей, 13б, Отделение общей врачебной практики (семейной медицины) №4': 'Корпус 3',
        'Городская поликлиника 11, Корпус 3, ул.Машиностроителей, 13Б Отделение акушерско-гинекологического профиля': 'Корпус 3',
        'Городская поликлиника 3, Корпус 1, Отделение медицинской профилактики': 'Корпус 1',
        'Городская поликлиника 3, Корпус 4 Отделение женской консультации ул Геращенко, 3, Акушерско-гинекологическое отделение': 'Женская консультация',
        'Городская поликлиника 3, Отделение амбулаторно-поликлинической помощи №1, Корпус 2 (ул Шишкова, 71)': 'Корпус 2',
        'Городская поликлиника 3, Отделение амбулаторно-поликлинической помощи №2, Корпус 6 (ул Остроухова, 1)': 'Корпус 6',
        'Городская поликлиника 3, Отделение женской консультации (ул Геращенко, 3)': 'Женская консультация',
        'ГП 11, ДП 8 (ул. Машиностроителей, 76)': 'ДП 8',
        'ГП 3, ДП 1 (пер. Ботанический, 49)': 'ДП 1',
        'ГП 3, ДП 1, Консультативно-диагностическое отделение №1': 'ДП 1',
        'ГП 3, ДП 1, Консультативно-диагностическое отделение №2': 'ДП 1',
        'ГП 3, ДП 1, Профилактическое отделение': 'ДП 1',
        'ГП 3, ДП 1, Профилактическое отделение, Отделение организации медицинской помощи несовершеннолетним в образовательных организациях, Медицинский персонал по обслуживанию детских садов': 'ДП 1',
        'ГП 3, ДП 1, Профилактическое отделение, Отделение организации медицинской помощи несовершеннолетним в образовательных организациях, Медицинский персонал по обслуживанию школ': 'ДП 1',
        'ГП 3, ДП 1, Профилактическое отделение, Центр здоровья для детей (ЦЗ)': 'ДП 1',
        'ГП 3, Корпус 1 , Общеполиклинический медицинский персонал': 'Корпус 1',
        'ГП 3, корпус 1, ОНМП №1, Отделение неотложной медицинской помощи 1 Кабинет травматологии и ортопедии': 'Корпус 1',
        'ГП 3, Корпус 1, Отделение дневного стационара': 'Корпус 1',
        'ГП 3, Корпус 1, Отделение инструментально-диагностических методов исследования': 'Корпус 1',
        'ГП 3, Корпус 1, Отделение общей врачебной практики (семейной медицины) №2': 'Корпус 1',
        'ГП 3, Корпус 1, Отделение общей врачебной практики (семейной медицины) №3': 'Корпус 1',
        'ГП 3, Корпус 1, Отделение первичной специализированной медицинской помощи': 'Корпус 1',
        'ГП 3, Корпус 1, Хирургическое отделение': 'Корпус 1',
        'ГП 3, Корпус 2 ул Шишкова, 71, Отделение общей врачебной практики (семейной медицины) №5': 'Корпус 2',
        'ГП 3, Корпус 2, Отделение амбулаторо-поликлинической помощи №1, общеполиклиический медицинский персонал': 'Корпус 2',
        'ГП11, Корпус №3, Кабинет инструментально-диагностических методов исследования': 'Корпус 3',
        'Детская поликлиника 8 Консультативно-диагностическое отделение 1 Дневной стационар': 'ДП 8',
        'Детская поликлиника №8, Консультативно-диагностическое отделение 1': 'ДП 8',
        'ДП 1, Консультативно-диагностическое отделение 1, Дневной стационар': 'ДП 1',
        'Кабинет медико-психологического консультирования': 'Корпус 1',
        'Кабинет неотложной медицинской помощи отделения неотложной медицинской помощи 1, корпус 1 пер.Ботанический 47': 'Корпус 1',
        'Общеучрежденческий медицинский персонал, Отдел экспертизы и контроля качества медицинской помощи;': 'рпус 1',
        'Общеучрежденческий медицинский персонал, Отделение медицинской профилактики для взрослоых': 'Корпус 1',
        'Общеучрежденческий медицинский персонал, Отделение медицинской профилактики для взрослых, Кабинет организации диспансеризации и профилактических медицинских осмотров Городской поликлиники №3': 'Корпус 1',
        'Отделение организации медицинской помощи детям в образовательных учреждениях, Медицинский персонал по обслуживанию школ': 'Корпус 1',
        'Психотерапевтический кабинет': 'Корпус 1',
        'Центр медико-социальной поддержки беременных, оказавшихся в трудной жизненной ситуации': 'Женская консультация',
    }

    def update_df(df):
        filtered_df = df[
            (df['Наименование МО'] == 'БУЗ ВО "ВГП № 3"') &
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
