from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


class Pokemon:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, hp):
    self.name = name
    self.type = type
    self.description = description
    self.hp = hp

pokemons = [
  Pokemon('Bulbasaur', 'grass', 'The cabage frog.', 37),
  Pokemon('Charmander', 'fire', 'The warm lizard.', 32),
  Pokemon('Squirtle', 'water', 'The fiesty turle.', 36)
]


# Define the home view
def home(request):
  return HttpResponse('<h1>Gotta Collect em All</h1>')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  return render(request, 'pokemons/index.html', { 'pokemons': pokemons })