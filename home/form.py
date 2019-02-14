from django import forms
from .models import Home

class Home_form(forms.ModelForm):

    class Meta:
        model = Home
        fields = ('nama', 'images','harga', 'deskripsi1', 'deskripsi2','deskripsi3','deskripsi4','deskripsi5',)
