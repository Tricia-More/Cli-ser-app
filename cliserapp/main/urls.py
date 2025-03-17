from django.urls import path
from .views import hello_world, weather, nam, ask, resp

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('weather/', weather, name='weather'),
    path('nam/', nam, name='nam'),
    path('ask/', ask, name="name" ),
    path('resp/',resp, name='resp'),
]