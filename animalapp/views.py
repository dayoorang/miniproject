from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from animalapp.forms import AnimalCreationForm
from animalapp.models import Animal


def index(request):
   return render(request,'animalapp/index.html')


def create(request):
   return render(request,'animalapp/create.html')

class AnimalCreateView(CreateView):
   model = Animal
   form_class = AnimalCreationForm
   template_name = 'animalapp/create.html'

   def get_success_url(self):
      return reverse('animalapp:detail', kwargs={'pk': self.object.pk})


class AnimalDetailView(DetailView):
   model = Animal
   context_object_name = 'target_animal'
   template_name = 'animalapp/detail.html'

