# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

LEVEL_CHOICES = (('beginner', 'Beginner'),
                     ('intermediate', 'Intermediate'),
                     ('expert', 'Expert'))


class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()
    description = models.TextField()
    level = models.CharField(choices=LEVEL_CHOICES,max_length=100)
    prerequisite_needed = models.BooleanField()
    prerequisite_description = models.TextField()


    def __str__(self):
        return self.name


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/')




