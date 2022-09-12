from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# Login form for user
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 'placeholder': 'Password'
            }
        )
    )


# Registration form for user
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 'placeholder': 'Username'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 'placeholder': 'Password having minimum 8 characters'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", 'placeholder': 'Confirm your password'
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 'placeholder': 'yahoo@gmail.com'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_doctor', 'is_patient')


# class AdminForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
#             'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mail ID'}),
#
#         }
