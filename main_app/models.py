from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Berries'),
  ('P', 'Poffin'),
  ('M', 'Moo Moo Milk')
)

class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  hp = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('pokemon-detail', kwargs={'pokemon_id': self.id})
  
class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )