from django.db import models

# Create your models here.

class registrat(models.Model):
    username = models.CharField( max_length=300)
    email = models.CharField( max_length=300)

  #  def __str__(self):
  #      return f" Событие {self.id}: {self.task}, дата:{self.dt_field}"
