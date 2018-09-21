# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.
# def show_home_page(request):
#     return HttpResponse("<h1>Hello</h1>");
def show_home_page(request):
    name = 'valera'
    list_names = ['Valera','Oleg','Mandarin']
    return render(request, 'home/index.html', context={'name':name, 'post':post});
