from django.db import models

# Create your models here.

class New_event(models.Model):
    task = models.CharField( max_length=300)
    dt_field = models.DateTimeField()

    def __str__(self):
        return f" Событие {self.id}: {self.task}, дата:{self.dt_field}"
