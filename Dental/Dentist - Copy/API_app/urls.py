from django.urls import re_path as url
from .import views

urlpatterns = [
    url(r'^api/patients$', views.patient_list),
    url(r'^api/patients/(?P<pk>[0-9]+)$', views.patient_detail),
]
