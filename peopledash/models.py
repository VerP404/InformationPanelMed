from django.db import models


class RegisteredPatients(models.Model):
    subdivision = models.CharField(max_length=50)
    speciality = models.CharField(max_length=255)
    slots_today = models.IntegerField()
    free_slots_today = models.IntegerField()
    slots_14_days = models.IntegerField()
    free_slots_14_days = models.IntegerField()
    report_datetime = models.CharField(max_length=50, default='-')

    def __str__(self):
        return self.speciality
