from django.shortcuts import render
from django.http import HttpResponse
from .models import Gatunek, Filmy


def index(request):
    gatunki = Gatunek.objects.all()

    return HttpResponse(gatunki)


def gatunek(request, id):
    gatunek_user = Gatunek.objects.get(pk=id)
    return HttpResponse(" " + gatunek_user.nazwa)

def film(request, id):
    film_user = Filmy.objects.get(pk=id)
    napis = "<h1>"+ str(film_user.tytul)+"</h1>" + \
            "<p>"+str(film_user.opis)+"</p>" + \
            "<p>"+str(film_user.rok_produkcji)+"</p>" + \
            "<p>"+str(film_user.ocena)+"</p>" + \
            "<p>"+str(film_user.rezyser)+"</p>"
    return HttpResponse(napis)
