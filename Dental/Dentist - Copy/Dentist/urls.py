from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
# from django_db_log import urls as django_db_log_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^', include('API_app.urls')),
    path('', include('Patient_app.urls')),
    path('', include('Dentist_app.urls')),
    path('', include('App_Admin.urls')),
    path('', include('Account.urls')),
    # url(r'^', include(django_db_log_urls)),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
