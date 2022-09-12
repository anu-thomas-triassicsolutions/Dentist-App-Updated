from django.db import models

from Account.models import User


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='services')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserActivity(models.Model):
    messages = models.CharField(max_length=250)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.messages
