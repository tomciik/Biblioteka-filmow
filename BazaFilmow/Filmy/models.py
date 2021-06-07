from django.db import models

# Create your models here.

class Rezyser(models.Model):
    imie = models.CharField(max_length=15)
    nazwisko = models.CharField(max_length=25)
    pochodzenie = models.CharField(max_length=25)

    def __str__(self):
        return self.imie, self.nazwisko

    class Meta:
        verbose_name = "Reżyser"
        verbose_name_plural = "Reżyser"

class Gatunek(models.Model):
    nazwa = models.CharField(max_length=30)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunek"

class Filmy(models.Model):

    tytul = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    ocena = models.DecimalField(max_digits=1, decimal_places=1)
    rezyser = models.ForeignKey(Rezyser, on_delete=models.CASCADE, null=True)
    gatunek = models.ManyToManyField(Gatunek)

    def __str__(self):
        return self.tytul

    class Meta:
        verbose_name = "Filmy"
        verbose_name_plural = "Filmy"
