from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()
    location = models.CharField(max_length=200)