from django.contrib import admin


# Register your models here.

from .models import Movie, Genre, FavouriteMovie, Viewer

admin.site.register(Viewer)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(FavouriteMovie)