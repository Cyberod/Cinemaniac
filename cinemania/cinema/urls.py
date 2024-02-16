from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
#    path('movies/<str:pk>/', views.movies, name='movies'),
    path('createfav/', views.CreateFav, name='createfav'),
    path('genre_movies/<int:genre_id>/', views.genre_movies, name='genre_movies'),
    path('remove_fav/<int:viewer_id>/', views.remove_fav, name='remove_fav'),
]