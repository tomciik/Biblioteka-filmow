from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gatunek, Filmy, Rezyser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login


def index(request):
    gatunki = Gatunek.objects.all()
    dane = {'gatunki': gatunki}
    return render(request, 'szablon.html', dane)


def gatunek(request, id):
    gatunek_user = Gatunek.objects.get(pk=id)
    gatunek_film = Filmy.objects.filter(gatunek = gatunek_user)
    gatunki = Gatunek.objects.all()
    dane = {'gatunek_user': gatunek_user,
            'gatunek_film': gatunek_film,
            'gatunki': gatunki}
    return render(request, 'gatunek_film.html', dane)


def film(request, id):
    film_user = Filmy.objects.get(pk=id)
    gatunki = Gatunek.objects.all()
    dane = {'film_user': film_user, 'gatunki': gatunki }
    return render(request, 'film.html', dane)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        film = Filmy.objects.filter(tytul__contains=searched)
        gatunki = Gatunek.objects.all()
        dane = {'searched': searched, 'film': film, 'gatunki': gatunki}
        return render(request, 'search.html', dane)
    else:
        return render(request, 'search.html', {})

def rezyser(request, id):
    rezyserzy = Rezyser.objects.get(pk=id)
    gatunki = Gatunek.objects.all()
    dane = {'rezyserzy': rezyserzy, 'gatunki': gatunki}
    return render (request, 'rezyser.html', dane)
