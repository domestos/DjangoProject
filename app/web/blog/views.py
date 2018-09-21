# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
# Create your views here.

def show_blog_page(request):
    name = 'valera'
    posts= Post.objects.all()
    list_names = ['Valera','Oleg','Mandarin']
    return render(request, 'blog/index.html', context={'name':name, 'posts':posts });

def __str__(self):
        return '{}'.format(self.title)
