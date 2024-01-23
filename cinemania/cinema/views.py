from django.shortcuts import render

# Create your views here.
from .models import Movies

genres = [
    {'id': 1, 'name':'Movie 1'},
    {'id': 2, 'name':'Movie 2'},
    {'id': 3, 'name':'Movie 3'},
]


def home(request):
    context = {'genres': genres}
    return render(request, 'cinema/home.html', context)


def movies(request, pk):
    
    film = None

    for i in genres:
        if i['id'] == int(pk):
            film = i

    context = {'movies': film}        

    return render(request, 'cinema/movies.html', context)                                                               
