from django.urls import path
from . import views


urlpatterns = [
    # path('login/', views.login_view, name='login_view'),
    # path('register/', views.register, name='register_view'),
    # path('logout/', views.logout, name='logout'),
    path('app_admin/', views.app_admin, name='adminpage'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),
    path('admin_patient_list/', views.admin_patient_list, name='admin_patient_list'),
    path('profile1/<int:user_id>/', views.profile1, name='profile1'),
    path('register_view_admin/', views.register_for_admin, name='register_view_admin'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('messages/', views.messages, name='messages'),
    path('delete_message/<int:patient_id>/', views.delete_message, name='delete_message'),
    path('add_service/', views.add_service, name='add_service'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('user_activity/', views.user_activities, name='user_activity'),
    path('doctor_activity/', views.doctor_activity, name='doctor_activity'),
    path('patient_activity/', views.patient_activity, name='patient_activity'),
    path('delete_activity/', views.delete_activity, name='delete_action'),
]
