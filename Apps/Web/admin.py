from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Slider)
admin.site.register(CollectionCenter)
admin.site.register(Categoria)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)