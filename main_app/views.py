from django.shortcuts import render
from .models import Pokemon
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  pokemons = Pokemon.objects.all()
  return render(request, 'pokemons/index.html', { 'pokemons': pokemons })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  return render(request, 'pokemons/detail.html', { 'pokemon': pokemon })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'
  success_url = '/pokemons/'

class PokemonUpdate(UpdateView):
  model = Pokemon
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['description', 'hp']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemons/'