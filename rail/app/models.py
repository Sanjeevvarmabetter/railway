from django.db import models
from . import User
# Create your models here.

class Train(models.Model):
    name = models.CharField(max_length=100)

class Station(models.Model):
    name = models.CharField(max_length=100)

class Ticket(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
