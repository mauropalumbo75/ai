from django.contrib import admin
from django.urls import include, path
from tictactoe import views

urlpatterns = [
    path('', views.tictactoe, name='tictactoe'),
]