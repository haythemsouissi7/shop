from django import forms
from django.contrib.auth.models import User

from .models import Album,Picture




class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['image' ]

class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ['logo' ]

