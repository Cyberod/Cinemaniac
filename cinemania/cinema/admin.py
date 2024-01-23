from django.contrib import admin


# Register your models here.

from .models import Movies, Genres, Favourites

admin.site.register(Movies)
admin.site.register(Genres)
admin.site.register(Favourites)