from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def get_absolute_url(self):
        return reverse('genre_movies', args=[str(self.id)])
    def __str__(self): 
        return self.name
    
    

class FavouriteMovie(models.Model):

    STATUS = (
        (True, 'favourite'),
        (False, 'not favourite')
        )

    created = models.DateTimeField(auto_now_add=True, null=True)
    owned = models.ForeignKey('Viewer', null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', null=True, on_delete=models.CASCADE) # might need to change it to a manytomanykey because i would also want to access the list of favourite movies a user has
    status = models.BooleanField(default=False, choices=STATUS)

    def __str__(self):
        return f'{self.owned.F_name} -- {self.owned.is_favourite}'


    class Meta:
        unique_together = ('owned', 'movie' )

class Movie(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    genre = models.ManyToManyField(Genre, related_name='movies' )
    release_date = models.DateField(null=True)
    #favourited_movie = models.ForeignKey(FavouriteMovie, on_delete=CASCADE)

    def __str__(self):
        return self.title



class Viewer(models.Model):
    F_name = models.ForeignKey(User, on_delete=models.CASCADE)
    L_name = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=200, null=True)
    is_favourite = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    viewer_joined = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        unique_together = ('F_name', 'is_favourite' )


    def __str__(self):
        return self.F_name.username
    

@receiver(post_save, sender=Viewer)
def update_favourite_movie(sender, instance, **kwargs):
    if instance.is_favourite:
        # If the Viewer's is_favourite field is set, create or update the FavouriteMovie entry
        FavouriteMovie.objects.update_or_create(owned=instance, movie=instance.is_favourite, defaults={'status': True})
    else:
        # If the Viewer's is_favourite field is cleared, delete the corresponding FavouriteMovie entry
        FavouriteMovie.objects.filter(owned=instance).delete()