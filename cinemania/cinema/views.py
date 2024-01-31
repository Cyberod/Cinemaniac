from django.shortcuts import render, redirect
from .models import Movies, Favourites
from .forms import FavouriteForm
# Create your views here.


#genres = [
#    {'id': 1, 'name':'Movie 1'},
#   {'id': 2, 'name':'Movie 2'},
#    {'id': 3, 'name':'Movie 3'},
#]


def home(request):
    movies = Movies.objects.all()
    favourites = Favourites.objects.all()
    context = {'movies': movies,
                'favourites': favourites}
    return render(request, 'cinema/home.html', context)


def movies(request, pk):
    film = Movies.objects.get(id=pk)

    context = {'movies': film}        

    return render(request, 'cinema/movies.html', context)                                                               


def createFavourite(request):
    form = FavouriteForm()
    if request.method == 'POST':
        form = FavouriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    

    context = {'form': form}
    return render(request, 'cinema/createfav.html', context)


def UpdateFavouritr(request, pk):
    pass