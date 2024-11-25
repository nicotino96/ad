from django.db import models

class CustomUser(models.Model):
    e_mail = models.CharField(max_length=290, unique=True)
    username = models.CharField(max_length=200)
    encrypted_password = models.CharField(max_length=120)

class UserSession(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(unique=True, max_length=35)

class Category(models.Model):
    title = models.CharField(max_length=60, unique=True)
    def __str__(self):
        return self.title


class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2400)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=1400)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)