from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required

from .models import Genre, Movie, Viewer, FavouriteMovie
from .forms import AddViewerFavForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def logoutUser(request):
    logout(request)
    return redirect('/')


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('/')

    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
    
    context = {'page': page}

    return render(request, 'cinema/login_register.html', context)


def registerPage(request):
    
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #To catch the user credentials like email or username and format it
            user.username = user.username.lower() #set the username to lower case
            #user.email = user.email.lower() #set the email to lower case
            user.save() #save the user credentials
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'An error occured during registration')
    context = {'form': form}
    return render(request, 'cinema/login_register.html', context)



def home(request):
    genres = Genre.objects.all()
    favourited = FavouriteMovie.objects.all()
    viewers = Viewer.objects.all()
    movies = Movie.objects.all()

    context = {'genres': genres, 'favourited': favourited, 'viewers': viewers, 'movies': movies}
    return render(request, 'cinema/home.html', context)


@login_required(login_url='/login/')
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
    movies = genre.movies.all() # used the related name movies to access the list of movies

    context = {'genre': genre, 'movies': movies}
    return render(request, 'cinema/genre_movies.html', context)


@login_required(login_url='/login/')
def remove_fav(request, viewer_id):

    viewer = get_object_or_404(Viewer, id=viewer_id)


    # Remove the viewers favourite movie and update the viewer
    viewer.is_favourite = None
    viewer.save()

    # Update the FavouriteMovie model
    FavouriteMovie.objects.filter(owned=viewer).update(status=False)


    return redirect('/')






















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

