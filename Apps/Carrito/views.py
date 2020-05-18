from django.shortcuts import render, redirect

# Create your views here.
from Apps.Web.models import Product
#from web.models import Cliente

from .models import Cart, CartItem

from django.contrib.auth.decorators import login_required


@login_required
def view(request):
    cart = Cart.objects.filter(user = request.user)
    
    cart_items = CartItem.objects.filter(cart__in = Cart.objects.filter(user = request.user))
    print(cart_items)
    return render(request, "carrito/view.html", {'cart_items' : cart_items})
'''     
def update_cart(request, slug):
    client_id = request.session['client_id']
    client = Cliente.objects.get(id=client_id)

    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False
    try: 
        cart = Cart.objects.get(client=client)
    except:
        new_cart = Cart()
        new_cart.client = client
        new_cart.save()
    
    cart = Cart.objects.get(client=client) #Se obtiene el objeto Cart con el ID especifico

    try:
        product = Product.objects.get(slug=slug)#Se obtiene el objeto Product con el slug que le pasamos en la URL
    except Product.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)#Se crea o se obtiene el objeto CartItem con los valores pasados en la funcion

    if created != True:
        if update_qty and qty:
            if int(qty) <= 0:  
                cart_item.delete()
            else:
                cart_item.quantity += int(qty)
                cart_item.save()
        else:
            pass
    else:
        if update_qty and qty:
            if int(qty) <= 0:
                cart_item.delete()
            else:
                cart_item.quantity = int(qty)
                cart_item.save()



    new_total = 0.00
    for item in cart.cartitem_set.all():#Obtiene todos los objetos Cart con el ID determinado en el modelo CartItem 
        line_total = float(item.product.price) * item.quantity
        new_total += line_total
    
    cart.total = new_total
    cart.save()
    
    total_products = 0
    for item in cart.cartitem_set.all():#Obtiene todos los objetos Cart con el ID determinado en el modelo CartItem 
        total_products += item.quantity

    request.session['items_total'] = total_products

    return redirect('index')
''' 