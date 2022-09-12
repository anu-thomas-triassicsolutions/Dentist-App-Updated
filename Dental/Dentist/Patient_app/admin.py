from django.contrib import admin
from Patient_app.models import Appointment, NewAppointmentForPatientLoggedIn

admin.site.register(Appointment)
admin.site.register(NewAppointmentForPatientLoggedIn)