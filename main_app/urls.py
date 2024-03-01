from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pokemons/', views.pokemon_index, name='pokemon-index'),
  path('pokemons/<int:pokemon_id>/', views.pokemon_detail, name='pokemon-detail'),
  path('pokemons/create/', views.PokemonCreate.as_view(), name='pokemon-create'),
  path('pokemons/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon-update'),
  path('pokemons/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon-delete'),
  path('pokemons/<int:pokemon_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
  path('pokemons/<int:pokemon_id>/assoc-toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
]