from django.db import models
from Account.models import User


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.IntegerField(blank=True)
    disease = models.CharField(max_length=100)
    prescription = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    created_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name


class NewAppointmentForPatientCreated(models.Model):
    improvement = models.CharField(max_length=150, blank=True)
    prescription = models.TextField(blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1)
    created_on = models.DateField(auto_now_add=True)
    created_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.improvement



