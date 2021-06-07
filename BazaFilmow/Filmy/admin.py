from django.contrib import admin
from .models import Filmy, Rezyser, Gatunek

# Register your models here.
admin.site.register(Filmy)
admin.site.register(Rezyser)
admin.site.register(Gatunek)