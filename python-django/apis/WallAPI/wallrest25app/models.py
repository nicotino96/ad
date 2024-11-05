from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=140)
    content = models.CharField(max_length=5500)
    publication_date = models.DateTimeField(auto_now=True)
