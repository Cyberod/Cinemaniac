from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Movies(models.Model):
    #viewer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    genre_name = models.ForeignKey('Genres', on_delete=models.SET_NULL, null=True, blank=True) 
    description = models.TextField(null=True, blank=True)
    favourite_status = models.ForeignKey('Favourites', on_delete=models.SET_NULL, null=True, blank=True, default=False)
    #updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']




    def __str__(self):
        return self.name


    

class Genres(models.Model):
    genre_name = models.TextField(null=True, blank=True)
    genre_id = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.genre_name

   

class Favourites(models.Model):
    movie_name = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    genres = models.ForeignKey(Genres, on_delete=models.CASCADE)
    #movie_description = models.TextField(null=True, blank=True)
    #movie_id = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __bool__(self):
        return self.status