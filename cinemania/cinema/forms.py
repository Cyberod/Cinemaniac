from django.forms import ModelForm
from .models import Viewer
from django.contrib.auth.models import User


class AddViewerFavForm(ModelForm):
    class Meta:
        model = Viewer
        fields = ['F_name', 'is_favourite']