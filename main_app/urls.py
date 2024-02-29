from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pokemons/', views.pokemon_index, name='pokemon_index'),
  path('pokemons/<int:pokemon_id>/', views.pokemon_detail, name='pokemon-detail'),
]