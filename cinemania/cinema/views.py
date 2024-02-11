from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required

from .models import Genre, Movie, Viewer, FavouriteMovie
from .forms import AddViewerFavForm

# Create your views here.


#genres = [
#    {'id': 1, 'name':'Movie 1'},
#   {'id': 2, 'name':'Movie 2'},
#    {'id': 3, 'name':'Movie 3'},
#]


def home(request):
    genres = Genre.objects.all()
    favourited = FavouriteMovie.objects.all()
    viewers = Viewer.objects.all()
    movies = Movie.objects.all()

    #favourite_movies = FavouriteMovie.objects.filter(viewer=viewer_instance)

    #favourite_movies = viewer_instance.favourites.prefetch_related('movie').all()


    


    context = {'genres': genres, 'favourited': favourited, 'viewers': viewers, 'movies': movies}
    return render(request, 'cinema/home.html', context)


def CreateFav(request):
    form = AddViewerFavForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        

    context = {'form': form}
    return render(request, 'cinema/createfav.html', context)


def genre_movies(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    movies = genre.movies.all() # I used the related name movies to access the list of movies

    context = {'genre': genre, 'movies': movies}
    return render(request, 'genre_movies.html', context)



# @login_required  # Requires the user to be logged in
# def add_favorite_movie(request, movie_id):
#     # Retrieve the user based on the request
#     user = request.user

#     # Retrieve the movie based on the movie_id parameter
#     movie = get_object_or_404(Movie, pk=movie_id)

#     # Check if the user has already marked the movie as a favorite
#     existing_favorite = FavouriteMovie.objects.filter(owned=user, movie=movie).exists()

#     if not existing_favorite:
#         # If not already marked as a favorite, create a new FavouriteMovie entry
#         FavouriteMovie.objects.create(owned=user, movie=movie, status=True)

#     # Redirect or render as needed
#     return render(request, 'success_template.html', {'movie': movie})

