from django.urls import path
from .views import hello_world, weather, nam

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('weather/', weather, name='weather'),
    path('nam/', nam, name='nam'),
]