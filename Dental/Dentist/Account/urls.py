from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register_view'),
    path('logout/', views.logout, name='logout'),
    # path('app_admin/', views.app_admin, name='adminpage'),
    # path('doctor_list/', views.doctor_list, name='doctor_list'),
    # path('admin_patient_list/', views.admin_patient_list, name='admin_patient_list'),
    # path('profile1/<int:id>/', views.profile1, name='profile1'),
    # path('registeradmin/', views.register_for_admin, name='register_view_admin'),
    # path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]
