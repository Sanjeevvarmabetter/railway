from django.db import models
from django.contrib.auth.models import User  # Corrected import statement

class Train(models.Model):
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100, default='Some Default Value')

    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=100)

class Ticket(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
