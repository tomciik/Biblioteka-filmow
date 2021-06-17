from django import forms
from django.forms import ModelForm
from .models import Filmy


class FilmForm(ModelForm):
    class Meta:
        model = Filmy
        fields = ('tytul', 'opis', 'rok_produkcji', 'ocena', 'rezyser', 'gatunek')
        labels = {
            'tytul': '',
            'opis': '',
            'rok_produkcji': '',
            'ocena': '',
        }
        widgets = {
            'tytul': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Podaj tytuł filmu'}),
            'opis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opisz film'}),
            'rok_produkcji': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Podaj rok produkcji'}),
            'ocena': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Podaj ocene'}),
            'rezyser': forms.Select(),
            'gatunek': forms.CheckboxSelectMultiple()
        }