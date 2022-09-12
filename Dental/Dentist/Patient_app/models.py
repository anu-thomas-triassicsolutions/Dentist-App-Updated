
from django.db import models
from django.conf import settings

from Account.models import User


class Appointment(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    my_doctor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='doctor_name')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='patient_name')

    def __str__(self):
        return self.date

    class Meta:
        db_table ='appointments'


class NewAppointmentForPatientLoggedIn(models.Model):
    disease = models.CharField(max_length=100, blank=True)
    improvement = models.CharField(max_length=150, blank=True)
    prescription = models.TextField(blank=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_on = models.DateField(auto_now_add=True)
    created_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.disease