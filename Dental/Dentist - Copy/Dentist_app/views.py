from django.shortcuts import render, redirect

from App_Admin.models import UserActivity
from Dentist_app.forms import PatientForm, DoctorUpdateForm
from Dentist_app.models import Patient, NewAppointmentForPatientCreated
from Account.models import User


# Home Page view
def index(request):
    if request.user.is_authenticated:
        if request.user is not None and request.user.is_superuser:
            return redirect('adminpage')
        elif request.user is not None and request.user.is_patient:
            return redirect('patient_home')
        else:
            return redirect('patient_list')
    return render(request, 'Index.html')


# Dentist Home Page view
def dentist_home(request):
    return render(request, 'Dentist Home.html')


# Adding patient data to database
def patient_data(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        disease = request.POST['disease']
        prescription = request.POST['prescription']
        patient = Patient(name=name, age=age, address=address, email=email,
                          phone=phone, disease=disease, prescription=prescription
                          )
        patient.save()
        print(patient.name)
        user_activity = UserActivity(name_id=request.user.id, messages=(request.user.username, ' added ',patient.name))
        user_activity.save()
    return render(request, 'Patient.html')  # Rendering values to html page


# patient list added by doctor
def patient_list(request):
    all_patients = Patient.objects.all()  # call all objects in patient
    appointment = User.objects.all()
    context = {'patient': all_patients, 'appointments': appointment}
    return render(request, 'Patient List.html', context)


# Detailed View of patient
def details(request, patient_id):
    data = Patient.objects.get(id=patient_id)
    return render(request, "Details.html", {"data": data})


# Delete a patient
def delete(request, patient_id):
    if request.method == "POST":
        patient = Patient.objects.get(id=patient_id)
        patient.delete()
        user_activity = UserActivity(name_id=request.user.id, messages=(request.user.username, ' deleted',patient.name))
        user_activity.save()
        return redirect('patient_list')
    return render(request, 'Delete.html')


# Update patient profile
def update(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        user_activity = UserActivity(name_id=request.user.id, messages=(request.user.username, ' updated', form.cleaned_data['name']))
        user_activity.save()
        return redirect('details', patient_id=patient_id)
    return render(request, 'Update.html', {'form': form, 'patient': patient})


# Take new appointment for patient
def appointment_for_patient_created(request, patient_id):
    if request.method == 'POST':
        improvement = request.POST['improvement']
        prescription = request.POST['prescription']
        # patient_created = Patient.objects.all()
        # if patient_id in patient_created:
        #     patient_created = Patient.objects.get(id=patient_id)
        #     print(patient)
        # else:
        #     patient_logged_in = User.objects.get(id=patient_id)
        #     print(patient_logged_in)
        patient = Patient.objects.get(id=patient_id)
        print(patient.name)
        appointment = NewAppointmentForPatientCreated(improvement=improvement, prescription=prescription, patient=patient)

        appointment.save()
        user_activity = UserActivity(name_id=request.user.id, messages=(request.user.username, ' created new appointment for', patient.name))
        user_activity.save()
        return redirect('details', patient_id=patient_id)
    return render(request, 'New Appointment.html')


# View appointment details
def appointment_view_for_patient_ceated(request, patient_id):
    appointment = NewAppointmentForPatientCreated.objects.filter(patient=patient_id)
    for i in appointment:
        print(i.patient)
        user_activity = UserActivity(name_id=request.user.id,
                                     messages=(request.user.username,' viewed appointments of ', i.patient.name))
        user_activity.save()
    return render(request, "All Appointment.html", {"appointments": appointment})


# Patient profiles  for doctor
def patient_profile(request):
    appointment = User.objects.all()
    return render(request, "Patient Profiles.html", {"appointments": appointment})


# detailed profile view of patient for doctor
def patient_profile_details(request, patient_id):
    patient = User.objects.get(id=patient_id)
    user_activity = UserActivity(name_id=request.user.id,
                                 messages=(request.user.username, ' viewed profile of ', patient.username))
    user_activity.save()
    return render(request, "Patient Profile.html", {"patient": patient})


# Update Doctor profile
def doctor_update(request, doctor_id):
    doctor = User.objects.get(id=doctor_id)
    form = DoctorUpdateForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('profile_view', doctor_id=doctor_id)
    return render(request, 'Update Patient.html', {'form': form, 'doctor': doctor})
