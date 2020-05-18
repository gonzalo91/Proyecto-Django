from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name="cart"),
    path('<slug:slug>', views.update_cart, name="update_cart"),

]
