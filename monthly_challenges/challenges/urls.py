from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('january', views.index),
    path('february', views.index2),
    path('<month>', views.challenge)
]
