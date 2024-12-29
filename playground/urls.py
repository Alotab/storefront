from django.urls import path
from . import views

urlpatterns = [
    path("", views.say_hello, name='home'),
    path("cache", views.cache_views, name='cache'),
]