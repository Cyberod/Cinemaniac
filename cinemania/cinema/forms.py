from django.forms import ModelForm
from.models import Movies, Genres, Favourites


class FavouriteForm(ModelForm):
    class Meta:
        model = Favourites
        fields = '__all__'