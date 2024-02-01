from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, null=True)
    











