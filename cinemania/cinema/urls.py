from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
#    path('movies/<str:pk>/', views.movies, name='movies'),
    path('createfav/', views.CreateFav, name='createfav'),
    path('genre_movies/<int:genre_id>/', views.genre_movies, name='genre_movies')
]