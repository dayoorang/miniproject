from django.contrib import admin

# Register your models here.
from animalapp.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass