from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_doctor = models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=True)


class Doctor(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
#
#
# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#
#     def __str__(self):
#         return self.user.username