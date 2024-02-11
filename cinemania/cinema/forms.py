from django.forms import ModelForm
from .models import Viewer


class AddViewerFavForm(ModelForm):
    class Meta:
        model = Viewer
        fields = ['F_name', 'is_favourite']