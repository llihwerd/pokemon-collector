from django.db import models
from django.urls import reverse

class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  hp = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('pokemon-detail', kwargs={'pokemon_id': self.id})