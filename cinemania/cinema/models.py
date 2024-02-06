from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self): 
        return self.name
    

class FavouriteMovie(models.Model):

    STATUS = (
        (True, 'favourite'),
        (False, 'not favourite')
        )

    created = models.DateTimeField(auto_now_add=True, null=True)
    #viewer = models.ForeignKey('Viewer', null=True, on_delete=CASCADE)
    movie = models.ForeignKey('Movie', null=True, on_delete=CASCADE) # might need to change it to a manytomanykey because i would also want to access the list of favourite movies a user has
    status = models.BooleanField(default=False, choices=STATUS)



class Movie(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField(null=True)
    favourited_movie = models.ManyToManyField(FavouriteMovie, related_name='favourites')

    def __str__(self):
        return self.title

### Yet to make migrations do remember

class Viewer(models.Model):
    F_name = models.ForeignKey(User, on_delete=models.CASCADE)
    L_name = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=200, null=True)
    is_favourite = models.ForeignKey(FavouriteMovie, on_delete=models.CASCADE, null=True)
    viewer_joined = models.DateTimeField(auto_now_add=True, null=True)