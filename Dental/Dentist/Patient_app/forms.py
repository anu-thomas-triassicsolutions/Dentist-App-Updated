from django import forms

from Patient_app.models import Appointment
from Account.models import User


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mail ID'}),

        }

#
# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = '__all__'
#         widgets = {
#             'date': forms.DateInput(),
#             'first_name': forms.TimeInput(),
#
#
#         }