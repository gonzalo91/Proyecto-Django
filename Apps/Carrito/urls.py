from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name="cart"),
    path('create-item-cart/<int:product>', views.create, name="create-item-cart"),
    path('delete-item-cart/<int:pk>', views.delete, name="delete-item-cart"),
    path('update-item-cart/<int:pk>', views.update, name="update-item-cart"),

]
