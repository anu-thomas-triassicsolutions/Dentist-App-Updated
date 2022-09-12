from django import forms
from.models import Patient
from Account.models import User


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'email', 'phone', 'disease', 'prescription' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mail ID'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'disease': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Disease '}),
            'prescription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'prescription'}),

        }




class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mail ID'}),

        }

