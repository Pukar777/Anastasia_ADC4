from django import forms

from .models import Movie


class OurForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('Movie_title', 'Movie_genre', 'Movie_price', 'Movie_image')
