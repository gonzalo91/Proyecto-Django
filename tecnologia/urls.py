"""tecnologia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Apps.Administracion.views import HomeApi, action_order

from Apps.Web.views import index_view, detalle_producto
from Apps.Carrito.views import view

urlpatterns = [
    path('', index_view, name="web.index"),

    path('producto/<int:pk>', detalle_producto, name="detalle_producto"),
    path('ct', view, name="cart"),

    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path(r'api/administrador/home', HomeApi.as_view()),
    path(r'api/administrador/action_order', action_order),

    path('administrador/', include('Apps.Administracion.urls'))
]
