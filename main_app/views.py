from django.shortcuts import render, redirect
from .models import Pokemon
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon
from .forms import FeedingForm



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  pokemons = Pokemon.objects.all()
  return render(request, 'pokemons/index.html', { 'pokemons': pokemons })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  feeding_form = FeedingForm()
  return render(request, 'pokemons/detail.html', {
    'pokemon': pokemon, 'feeding_form': feeding_form
  })

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

def add_feeding(request, pokemon_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.pokemon_id = pokemon_id
    new_feeding.save()
  return redirect('pokemon-detail', pokemon_id=pokemon_id)