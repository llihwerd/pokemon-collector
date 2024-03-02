from django.shortcuts import render, redirect
from .models import Pokemon
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon, Toy
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView



class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  pokemons = Pokemon.objects.all()
  return render(request, 'pokemons/index.html', { 'pokemons': pokemons })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  toys_pokemon_doesnt_have = Toy.objects.exclude(id__in = pokemon.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'pokemons/detail.html', {
    'pokemon': pokemon, 'feeding_form': feeding_form, 'toys': toys_pokemon_doesnt_have
  })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = ['name', 'type', 'description', 'hp']
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

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, pokemon_id, toy_id):
  Pokemon.objects.get(id=pokemon_id).toys.add(toy_id)
  return redirect('pokemon-detail', pokemon_id=pokemon_id)