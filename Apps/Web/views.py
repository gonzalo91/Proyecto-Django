from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError
from django.contrib import messages

from .models import *
from Apps.Carrito.models import Cart, CartItem

from Apps.Carrito.views import view as cart_view

from functools import reduce



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

@login_required
def checkout(request):
	if request.method == 'POST':
		cart = Cart.objects.filter(user = request.user)

		cart_items_checkout = CartItem.objects.filter(cart__in = cart ) 
		
		collection_centers = CollectionCenter.objects.filter(id__in = cart_items_checkout.values('product__collection_center'))

		for c_c in collection_centers:
			c_c.items_cart = list(filter(lambda x: x.product.collection_center == c_c, cart_items_checkout))

			
			c_c.total_cart = sum (map(lambda a:  a.subtotal(), c_c.items_cart) )
		
		return render(request, 'payments/index.html', 
						{'collection_centers' : collection_centers, })
		
	return redirect('carrito/')


@login_required
def make_order(request):
	
	try:
		collection_center = get_object_or_404(CollectionCenter, pk = request.POST['c_c'])

		cart = Cart.objects.filter(user = request.user)

		cart_items_order = CartItem.objects.filter(cart__in = cart, product__collection_center = collection_center ) 
		order = Order( user = request.user, collection_center = collection_center, status = 1, date_at = request.POST['date_at'])
		order.save()

		for item in cart_items_order:
			order_detail = OrderDetail( order = order,
			 							name= item.product.name, 
										donated = item.product.donated, 
										product = item.product, 
										price= item.product.price, 
										qty = item.quantity)
			order_detail.save()

		messages.success(request, 'Order Created')

		cart_items_order.delete()
		return redirect('/profile/order/' + str(order.id))
	except Exception as ex:
		raise Exception(repr(ex))

@login_required
def orders(request, pk):
	order = get_object_or_404(Order, pk = pk, user = request.user)

	order_details = OrderDetail.objects.filter(order = order)

	return render(request, 'profile/orders.html', 
						{'order' : order, 'order_details' : order_details })
	
