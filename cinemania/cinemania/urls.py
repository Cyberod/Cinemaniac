
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the cinemania index.")


def movies(request):
    return HttpResponse("Hello, world. You're now viewing all the movies.")                                                               




urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),
    path('movies/', movies),
]
