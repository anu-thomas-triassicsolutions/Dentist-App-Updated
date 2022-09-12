from django.contrib import admin

from App_Admin.models import Contact, Service, UserActivity

admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(UserActivity)
