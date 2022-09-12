from django.contrib import admin
from .models import Patient, NewAppointmentForPatientCreated

admin.site.register(Patient)
admin.site.register(NewAppointmentForPatientCreated)
