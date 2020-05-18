from django.urls import path
from . import views
from .Home import views as views_home

urlpatterns = [
    path('home', views.home_api),    
    path('action_order', views.action_order)
]