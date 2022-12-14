from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Album

import requests
import environ
env = environ.Env()
environ.Env.read_env()


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)



class AlbumSearch(forms.Form):
    artist = forms.CharField(label='artist', max_length=50)
    album = forms.CharField(label='album', max_length=50)

    def get_album(self):
        try:
            artist = self.cleaned_data.get('artist')
            album = self.cleaned_data.get('album')
            URL = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={env('API_KEY')}&artist={artist}&album={album}&format=json"
            response = requests.get(URL)
            data = response.json()

            return data

        except AttributeError:
            return data

        