from django.forms import ModelForm
from django import forms
from animalapp.models import Animal


class AnimalCreationForm(ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={"style" :"display:none",
                                                                   "name":"inpFile",
                                                                    "id":"inpFile" }))

    class Meta:
        model = Animal
        fields = '__all__'