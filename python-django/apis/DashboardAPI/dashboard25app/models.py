from django.db import models

class Dashboard(models.Model):
    title = models.CharField(max_length=140)
    summary = models.CharField(max_length=5500)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "summary": self.summary
        }


class Question(models.Model):
    DoesNotExist = None
    dashboard = models.ForeignKey(Dashboard,on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    summary = models.CharField(max_length=5500)
    publication_date = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "summary": self.summary,
            "publication_date": self.publication_date
        }


class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    description = models.CharField(max_length=5500)
    publication_date = models.DateTimeField(auto_now=True)
    def to_json(self):
        return {
            "description": self.description,
            "publication_date": self.publication_date
        }

# Create your models here.
