from django.shortcuts import render, redirect
from App_Admin.models import UserActivity
from Patient_app.forms import PatientUpdateForm
from Patient_app.models import Appointment, NewAppointmentForPatientLoggedIn
from Account.models import User


# Patient home view
def patient_home(request):
    return render(request, 'Patient Home.html')


# profile view for patient
def profile_view(request, patient_id):
    patient_data = User.objects.filter(id=patient_id)
    user_activity = UserActivity(name_id=request.user.id,
                                 messages=(request.user.username, ' Viewed profile '))
    user_activity.save()
    return render(request, 'My Profile.html', {'patient_data': patient_data})


# All patient list view
def patient_profile_list(request):
    all_patients = User.objects.all()  # call all objects
    user_activity = UserActivity(name_id=request.user.id,
                                 messages=(request.user.username, ' Viewed patients list '))
    user_activity.save()
    context = {'patient': all_patients}
    return render(request, 'Patient Profile List.html', context)  # Passing Objects to html page


# Update patient profile
def patient_update(request, patient_id):
    patient = User.objects.get(id=patient_id)
    form = PatientUpdateForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        user_activity = UserActivity(name_id=request.user.id,
                                     messages=(request.user.username, ' updated profile'))
        user_activity.save()
        return redirect('profile_view', patient_id=patient_id)
    return render(request, 'Update Patient.html', {'form': form, 'patient': patient})


#Appointment
def patient_appointment(request):
    """ Adding booking of a patient to database"""
    doctor = User.objects.filter(is_doctor=True)
    if request.method == 'POST':
        date = request.POST.get("date")
        time = request.POST.get("time")
        doctor_id = request.POST.get("doctor")
        patient = request.user.id
        print(request.user.id)
        print(f"doctor : {doctor_id}")
        # doctor = User.objects.filter(id=doctor_id)
        print(isinstance(doctor, User))
        doctor = User.objects.get(id=doctor_id)
        print(f"doctor instance : {doctor}")
        print(type(doctor))
        print(type(User))

        appointment = Appointment.objects.create(date=date, time=time, my_doctor_id=doctor_id, patient_id=patient)
        # appointment.my_doctor = doctor_id
        appointment.save()
        user_activity = UserActivity(name_id=request.user.id,
                                     messages=(request.user.username, ' Booked appointment for ', doctor.username, 'on', date))
        user_activity.save()
        return redirect('done')
    return render(request, 'Patient Appointment.html', {'doctors': doctor})


# Appointment list view to doctor via booking
def appointment_list(request):
    appointments = Appointment.objects.all().order_by('date')

    return render(request, "My Appointment.html", {"appointments": appointments})


# Booking Confirmation
def done(request):
    return render(request, 'Done.html')


# Take new appointment for patient
def appointment_for_patient_logged_in(request, patient_id):
    if request.method == 'POST':
        disease = request.POST['disease']
        improvement = request.POST['improvement']
        prescription = request.POST['prescription']
        patient = User.objects.get(id=patient_id)
        appointment = NewAppointmentForPatientLoggedIn(disease=disease, improvement=improvement,
                                                       prescription=prescription, patient=patient)
        appointment.save()
        print(patient.username)
        user_activity = UserActivity(name_id=request.user.id,
                                     messages=(request.user.username, ' Created new appointment for ', patient.username))
        user_activity.save()
        return redirect('patient_list')
    return render(request, 'Patient logged in.html')


# View appointment details
def appointment_view_for_patient_logged_in(request, patient_id):

    appointment = NewAppointmentForPatientLoggedIn.objects.filter(patient=patient_id)
    patient = User.objects.get(id=patient_id)
    print(patient)
    user_activity = UserActivity(name_id=request.user.id,
                                 messages=(request.user.username, ' viewd appointment list of ', patient.username))
    user_activity.save()
    return render(request, "Appointment View for patient logged in.html", {"appointments": appointment})



# def profile_view(request, profile_id):
#     """ Profile """
#     appointments = Appointment.objects.get(id=profile_id)
#     return render(request, "Profile.html", {"appointment": appointments})


# def appointment_view(request, appointment_id):
#     appointments = Appointment.objects.get(id=appointment_id)
#     return render(request, "Appointment View.html", {"appointment": appointments})

