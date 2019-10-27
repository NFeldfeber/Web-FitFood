from django.conf.urls import static
from django.contrib import admin
from django.urls import path

from FitFood_Web import settings
from Site import views

urlpatterns = [
    path('', views.index),
]
