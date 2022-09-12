from django.shortcuts import render, redirect
from Account.forms import SignUpForm
from Account.models import User
from App_Admin.forms import AdminForm
from App_Admin.models import Contact, Service, UserActivity


# User activity
def user_activities(request):
    """Fetching all user activities saved in database."""

    activities = UserActivity.objects.all().order_by('-id')
    if request.method == "POST":
        type = request.POST['user']
        if type == 'doctor':
            # u = User.objects.filter(is_doctor=True).values_list('id', flat=True)

            return redirect('doctor_activity')
        elif type =='patient':
            return redirect('patient_activity')
            # activities = UserActivity.objects.filter(name__is_patient=True)
        elif type =='all':
            return redirect('user_activity')
        elif type == None:
            activities = UserActivity.objects.all()
    elif request.method == None:
        activities = UserActivity.objects.all().order_by('-id')
    return render(request, 'Activities.html', {'activities': activities})


def doctor_activity(request):
    activities = UserActivity.objects.filter(name__is_doctor=True).order_by('-id')
    if request.method == "POST":
        type = request.POST['user']
        if type == 'doctor':
            return redirect('doctor_activity')
        elif type == 'patient':
            return redirect('patient_activity')
        elif type == 'all':
            return redirect('user_activity')

    return render(request, 'Doctor Activities.html', {'activities': activities})


def patient_activity(request):
    activities = UserActivity.objects.filter(name__is_patient=True).order_by('-id')
    if request.method == "POST":
        type = request.POST['user']
        if type == 'doctor':
            return redirect('doctor_activity')
        elif type == 'patient':
            return redirect('patient_activity')
        elif type == 'all':
            return redirect('user_activity')
    return render(request, 'Patient Activities.html', {'activities': activities})


# delete  all activities
def delete_activity(request):
    if request.method == "POST":
        action = UserActivity.objects.all()
        action.delete()
        return redirect('user_activity')
    return render(request, 'Delete Activity.html')


def app_admin(request):
    admin = User.objects.get(pk=1)
    users = User.objects.all()
    form = AdminForm(request.POST or None, instance=admin)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'Admin.html', {'form': form, 'admins': admin, 'users': users})


def profile1(request, user_id):
    user = User.objects.get(id=user_id)
    form = AdminForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        if user.is_doctor:
            return redirect('doctor_list')

        if user.is_patient:
            return redirect('admin_patient_list')
    return render(request, 'User Profie.html', {'form': form, 'account_user': user})


def register_for_admin(request):
    """ User registration for Doctor and Patient."""
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # msg = 'user created'
            if User.is_authenticated:
                if User is not None and User.is_superuser:
                    activity = UserActivity(name_id=request.user.id, messages="Admin added new user")
                    activity.save()
                    return redirect('register_for_admin')
            #  Emailing option for the registered user.
            # send_mail(
            #     'Test Mail',
            #     'Patient Signed up Successfully!!',
            #     'anu.thomas@triassicsolutions.com',
            #     [form.cleaned_data['email']],
            #     fail_silently=False,
            # )
            # print(form.cleaned_data['email'], msg)
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'Register.html', {'form': form, 'msg': msg})


def delete_user(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        user.delete()
        if user.is_doctor:
            activity = UserActivity(name_id=request.user.id, messages="Admin deleted a doctor")
            activity.save()
            return redirect('doctor_list')
        if user.is_patient:
            activity = UserActivity(name_id=request.user.id, messages="Admin added a patient")
            activity.save()
            return redirect('admin_patient_list')
    return render(request, 'Delete User.html')


def doctor_list(request):
    users = User.objects.all()
    return render(request, 'Doctor list.html', {'users': users})


def admin_patient_list(request):
    users = User.objects.all()
    return render(request, 'Admin-Patient List.html', {'users': users})


# Contact Option to the home page
def contact(request):
    """ Saving Contact information  to database """

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request. POST['message']
        form = Contact(name=name, email=email, message=message)
        form.save()
        activity = UserActivity(name_id=request.user.id, messages="You got a new message")
        activity.save()
        return redirect('index')
    return render(request, 'Contact Form.html')


# Contact view for doctor
def messages(request):
    patient = Contact.objects.all()
    return render(request, 'Messages.html', {'patients': patient})


# delete  contact massages
def delete_message(request, patient_id):
    if request.method == "POST":
        patient = Contact.objects.get(id=patient_id)
        patient.delete()
        return redirect('messages')
    return render(request, 'Delete.html')


# Dental Service
def add_service(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        description = request.POST['description']
        service = Service(name=name, image=image, description=description)
        service.save()
        activity = UserActivity(name_id=request.user.id, messages="Admin added new service")
        activity.save()
    return render(request, 'Add Services.html')


# Add services to web page
def services(request):
    service = Service.objects.all()
    return render(request, 'Our services.html', {'services': service})


def user_activity(request):
    activities = UserActivity.objects.all()
    
    return render(request, 'User Activity.html', {'activities': activities})
