from django.shortcuts import render

# Create your views here.
from .models import Movies

#genres = [
#    {'id': 1, 'name':'Movie 1'},
#   {'id': 2, 'name':'Movie 2'},
#    {'id': 3, 'name':'Movie 3'},
#]


def home(request):
    genres = Movies.objects.all()
    context = {'genres': genres}
    return render(request, 'cinema/home.html', context)


def movies(request, pk):
    film = Movies.objects.get(id=pk)

    context = {'movies': film}        

    return render(request, 'cinema/movies.html', context)                                                               
