from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('dentist_home/', views.dentist_home, name='dentist_home'),
    path('patient_profile',views.patient_profile, name='patient_profile'),
    path('patient_data/', views.patient_data, name='patient_data'),
    path('patient_list/', views.patient_list, name='patient_list'),
    path('details/<int:patient_id>/', views.details, name='details'),
    path('delete/<int:patient_id>/', views.delete, name='delete'),
    path('update/<int:patient_id>/', views.update, name='update'),
    path('new_appointment/<int:patient_id>/', views.appointment_for_patient_created, name='new_appointment'),
    path('appointment_details/<int:patient_id>/', views.appointment_view_for_patient_ceated, name='appointment_details'),
    path('patient_profile_details/<int:patient_id>/', views.patient_profile_details, name='patient_profile_details'),
    path('doctor_update/<int:doctor_id>/', views.doctor_update, name='doctor_update'),

]
