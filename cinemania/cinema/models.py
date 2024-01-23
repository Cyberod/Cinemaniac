from django.db import models

# Create your models here.


class Movies(models.Model):
    genre = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    #favourites
    #updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)