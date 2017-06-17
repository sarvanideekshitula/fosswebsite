# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here
from events.models import Event


def Events(request):
    template = 'event.html'
    object_list = Event.objects.all()
    context = {'object_list': object_list}
    return render(request, template, context)