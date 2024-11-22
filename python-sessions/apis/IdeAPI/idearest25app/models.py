from django.db import models

class CustomUser(models.Model):
    e_mail = models.CharField(max_length=290, unique=True)
    username = models.CharField(max_length=200)
    encrypted_password = models.CharField(max_length=120)

class UserSession(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(unique=True, max_length=35)

