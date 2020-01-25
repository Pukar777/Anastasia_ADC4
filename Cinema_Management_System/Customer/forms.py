from django import forms

from .models import MovieRequest


class OurForm(forms.ModelForm):
    class Meta:
        model = MovieRequest
        fields = ('title', 'releasedate', 'img')