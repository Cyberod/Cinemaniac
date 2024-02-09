from django.shortcuts import render, redirect

from .models import Genre, Movie, Viewer, FavouriteMovie
#from .forms import FavouriteForm
# Create your views here.


#genres = [
#    {'id': 1, 'name':'Movie 1'},
#   {'id': 2, 'name':'Movie 2'},
#    {'id': 3, 'name':'Movie 3'},
#]


def home(request):
    genres = Genre.objects.all()
    favourited = FavouriteMovie.objects.all()
    viewer_name = Viewer.objects.all()

    #favourite_movies = FavouriteMovie.objects.filter(viewer=viewer_instance)

    #favourite_movies = viewer_instance.favourites.prefetch_related('movie').all()


    


    context = {'genres': genres, 'favourited': favourited, 'viewer_name': viewer_name}
    return render(request, 'cinema/home.html', context)


