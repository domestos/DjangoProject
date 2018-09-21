from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url('',show_home_page),
]
