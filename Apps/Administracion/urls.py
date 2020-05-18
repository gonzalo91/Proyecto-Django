from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="admin.index"),          
    
    
    path('products', views.IndexView.as_view(), name='product_index'),    
    path('newproduct/', views.productview, name='new_product'),    
    path('product/edit/<int:pk>/', views.product_edit, name='product_edit'),    
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),


    path('clients', views.ClientView.as_view(), name="client_index"),
    path('orders', views.OrderView.as_view(), name="order_index"),
    path('orders/<int:pk>/', views.order_view, name="order_view"),
    #path('clientes/', views.clientes, name="clientes"),
 
]