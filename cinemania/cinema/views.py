from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required

from .models import Genre, Movie, Viewer, FavouriteMovie
from .forms import AddViewerFavForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import requests
from django.http import JsonResponse

# Create your views here.

def logoutUser(request):
    logout(request)
    return redirect('/')


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('/')

    if request.method== 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            #Authentication
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            # user = form.get_user()
            # login(request, user)
            # return redirect('/')


            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'Username does not exist')

    else:
        form = AuthenticationForm(request)

    context = {'page': page, 'form': form}

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
    return render(request, 'cinema/movie-list.html', context)


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




def proxy_api_request(request):
    api_url = "https://image.tmdb.org/t/p/"
    api_key = "92492102bdac5ee5e66f112789815a7e"  # Keep this secure on the server

    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        movies_data = response.json()
        return JsonResponse(movies_data)
    else:
        return JsonResponse({"error": "Failed to fetch data"}, status=500)









# views.py
# import requests
# from django.shortcuts import render

# def my_view(request):
#     api_url = "https://api.example.com/movies"
#     api_key = "your_api_key"  # Keep this secure on the server

#     headers = {"Authorization": f"Bearer {api_key}"}
#     response = requests.get(api_url, headers=headers)

#     if response.status_code == 200:
#         movies_data = response.json()
#     else:
#         movies_data = []

#     return render(request, 'my_template.html', {'movies_data': movies_data})














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

