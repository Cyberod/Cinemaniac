from django.shortcuts import render, redirect

from .models import Genre
#, Movie, Viewer, FavouriteMovie
#from .forms import FavouriteForm
# Create your views here.


#genres = [
#    {'id': 1, 'name':'Movie 1'},
#   {'id': 2, 'name':'Movie 2'},
#    {'id': 3, 'name':'Movie 3'},
#]


def home(request):
    genres = Genre.objects.all()

    # Assuming you have a Movie instance
   # movie_instance = Movie.objects.get(id=1)

    # Accessing genres associated with the movie
    #associated_genres = movie_instance.genres.all()

    # Iterating through genres

    viewer_instance = Viewer.objects.first()

    viewer_name = viewer_instance.F_name.username


    #favourite_movies = FavouriteMovie.objects.filter(viewer=viewer_instance)

    favourite_movies = viewer_instance.favourites.prefetch_related('movie').all()


    


    context = {'genres': genres, 'favourite_movies': favourite_movies, 'viewer_name': viewer_name}
    return render(request, 'cinema/home.html', context)


