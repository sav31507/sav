from django import forms
from .models import movie
# above (movie } from models.py defined


class MovieForm(forms.ModelForm):
    class Meta:
        model= movie
        fields=('name','year','des','image')