from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return self.name
