from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *


# Create your views here.
def index_view(request, *args, **kwargs):
	
	
	medicines = Product.objects.filter(type_product = Product.TYPES[2][0]).order_by('id')[:4]
	products = Product.objects.filter(type_product = Product.TYPES[0][0]).order_by('id')[:4]
	services = Product.objects.filter(type_product = Product.TYPES[1][0]).order_by('id')[:4]

	collection_centers = CollectionCenter.objects.all().order_by('id')[:8]
	
	return render(request, "home_web/index.html", { 'medicines' : medicines, 'products' : products,  'collection_centers' : collection_centers, 'services': services })

def about_view(request, *args, **kwargs):
	return render(request, "about.html",{})


def detalle_producto(request, pk):
	product = get_object_or_404(Product, pk = pk)

	products_related = Product.objects.filter(category = product.category).distinct()[:12]
	
	c_c_items = Product.objects.filter(collection_center= product.collection_center)[:12]
	
	return render(request, "detalle_producto.html", \
				{ 'product' : product, 'products_related' : products_related, 'c_c_items' : c_c_items })
