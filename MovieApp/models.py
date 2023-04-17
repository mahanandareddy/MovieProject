from django.db import models

class Movies(models.Model):
    release_date = models.DateField()
    movie = models.CharField(max_length=30)
    actor = models.CharField(max_length=30)
    actress = models.CharField(max_length=30)
    rating = models.IntegerField()

