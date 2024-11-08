from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=140)
    content = models.CharField(max_length=5500)
    publication_date = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "title": self.title,
            "content": self.content,
            "created": self.publication_date,
        }


class Comment(models.Model): # Nuevo modelo
    content = models.CharField(max_length=1900)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

    def to_json(self):
        return {
            "info": self.content,
        }
