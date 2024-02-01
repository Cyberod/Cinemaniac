from django.shortcuts import render, redirect

from .models import Movie
#from .forms import FavouriteForm
# Create your views here.


#genres = [
#    {'id': 1, 'name':'Movie 1'},
#   {'id': 2, 'name':'Movie 2'},
#    {'id': 3, 'name':'Movie 3'},
#]


def home(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'cinema/home.html', context)


