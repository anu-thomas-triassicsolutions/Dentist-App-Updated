from django.shortcuts import render, redirect

from App_Admin.models import UserActivity
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
# from django.core.mail import send_mail



def register(request):
    """ User registration for Doctor and Patient."""
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_authenticated:
                if request.user is not None and request.user.is_superuser:
                    msg = 'user created'
                    #  Emailing option for the registered user.
                    # send_mail(
                    #     'Test Mail',
                    #     'Patient Signed up Successfully!!',
                    #     'anu.thomas@triassicsolutions.com',
                    #     [form.cleaned_data['email']],
                    #     fail_silently=False,
                    # )
                    # print(form.cleaned_data['email'], msg)
                    user_activity = UserActivity(name_id=request.user.id, messages="Admin added a new User")
                    user_activity.save()
                    return redirect('adminpage')
            else:
                return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'Register.html', {'form': form, 'msg': msg})


def login_view(request):
    """ User authentication for Doctor and Patient."""
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print (form.cleaned_data['username'])
            user = authenticate(username=username, password=password)

            if user is not None and user.is_patient:
                print(user)
                user_activity = UserActivity(name_id=user.id, messages= (user.username,' logged in'))
                user_activity.save()
                login(request, user)
                return redirect('patient_home')
            elif user is not None and user.is_doctor:
                user_activity = UserActivity(name_id=user.id, messages=(user.username, ' logged in'))
                user_activity.save()
                login(request, user)
                return redirect('patient_list')
            elif user is not None and user.is_superuser:
                user_activity = UserActivity(name_id=user.id, messages=(user.username, ' logged in'))
                user_activity.save()
                login(request, user)
                return redirect('adminpage')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'Login.html', {'form': form, 'msg': msg})


def logout(request):
    """ User logout """
    user_activity = UserActivity(name_id=request.user.id, messages=(request.user.username, ' logged out'))
    user_activity.save()
    auth.logout(request,)
    return redirect('index')

