from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)  # custom password field

    def __str__(self):
        return self.username.username

