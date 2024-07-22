from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Корпус"
        verbose_name_plural = "Корпуса"

    def __str__(self):
        return self.name


class Subdivision(models.Model):
    name = models.CharField(max_length=100, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='subdivisions')

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='pages')
    subdivision = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title


class RegisteredPatients(models.Model):
    subdivision = models.CharField(max_length=50)
    speciality = models.CharField(max_length=255)
    slots_today = models.IntegerField()
    free_slots_today = models.IntegerField()
    slots_14_days = models.IntegerField()
    free_slots_14_days = models.IntegerField()
    report_datetime = models.CharField(max_length=50, default='-')

    class Meta:
        verbose_name = "Загруженные данные"
        verbose_name_plural = "Загруженные данные"

    def __str__(self):
        return f"{self.subdivision} - {self.speciality}"


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Краткое название')
    full_name = models.CharField(max_length=255, verbose_name='Полное название')
    logo = models.ImageField(upload_to='organization_logos/', verbose_name='Логотип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
