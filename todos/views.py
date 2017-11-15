# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    data = {'nom': 'Manel'}
    return render(request, 'todos/index.html', context=data)
