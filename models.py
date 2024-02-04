from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200)
    director=models.CharField(max_length=200)
    release_date=models.DateTimeField('relase date')
    genre=models.CharField(max_length=200)
    duration=models.FloatField()
    
    def __str__(self):
        return  self.title + "_ " + self.director