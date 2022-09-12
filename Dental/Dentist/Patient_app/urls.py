from .import views
from django.urls import path

urlpatterns = [
    path('patient_home/', views.patient_home, name='patient_home'),
    path('patient_profile_list/', views.patient_profile_list, name='patient_profile_list'),
    path('profile_view/<int:patient_id>/', views.profile_view, name='profile_view'),
    path('patient_update/<int:patient_id>/', views.patient_update, name='patient_update'),
    path('appointment/', views.patient_appointment, name="patient_appointment"),
    path('appointment/list/', views.appointment_list, name="appointment_list"),
    path('done/', views.done, name="done"),
    path('appointment_for/<int:patient_id>/', views.appointment_for_patient_logged_in, name='patient_logged_in'),
    path('appointment_view_for/<int:patient_id>/', views.appointment_view_for_patient_logged_in,
         name='appointment_view_for_patient_logged_in'),
    # path('profile_view/<int:profile_id>/', views.profile_view, name="profile_view"),
    # path('appointment_view/<int:appointment_id>/', views.appointment_view, name="appointment_view"),

]
