from django.contrib import admin
from django.urls import path

from animalapp.views import index, create, AnimalCreateView, AnimalDetailView

app_name = 'animalapp'
urlpatterns = [
    path('', index, name='main'),
    path('create/', AnimalCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AnimalDetailView.as_view(), name='detail'),

]