from django.shortcuts import render
from django.http import HttpResponse
from .models import Gatunek, Filmy


def index(request):
    gatunki = Gatunek.objects.all()
    dane = {'gatunki' : gatunki}
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
    dane = {'film_user' : film_user, 'gatunki' : gatunki }
    return render (request, 'film.html', dane)
