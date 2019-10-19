from django.contrib import admin
from django.urls import path, include
from . import views

# url for user registration
urlpatterns = [
    path('register', views.register, name='users-register')
]
