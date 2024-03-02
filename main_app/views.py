from django.shortcuts import render, redirect
from .models import Pokemon
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon, Toy
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def pokemon_index(request):
  pokemons = Pokemon.objects.filter(user=request.user)
  return render(request, 'pokemons/index.html', { 'pokemons': pokemons })

@login_required
def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  toys_pokemon_doesnt_have = Toy.objects.exclude(id__in = pokemon.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'pokemons/detail.html', {
    'pokemon': pokemon, 'feeding_form': feeding_form, 'toys': toys_pokemon_doesnt_have
  })

class PokemonCreate(LoginRequiredMixin, CreateView):
  model = Pokemon
  fields = ['name', 'type', 'description', 'hp']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PokemonUpdate(LoginRequiredMixin, UpdateView):
  model = Pokemon
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['description', 'hp']

class PokemonDelete(LoginRequiredMixin, DeleteView):
  model = Pokemon
  success_url = '/pokemons/'

@login_required
def add_feeding(request, pokemon_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.pokemon_id = pokemon_id
    new_feeding.save()
  return redirect('pokemon-detail', pokemon_id=pokemon_id)

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, pokemon_id, toy_id):
  Pokemon.objects.get(id=pokemon_id).toys.add(toy_id)
  return redirect('pokemon-detail', pokemon_id=pokemon_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('pokemon-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)