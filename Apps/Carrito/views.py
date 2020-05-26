from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import IsAuthenticated
from rest_framework.response    import Response

from Apps.Web.models import Product
from .models import Cart, CartItem



@login_required
def view(request):
    cart = Cart.objects.filter(user = request.user)
    
    cart_items = CartItem.objects.filter(cart__in = Cart.objects.filter(user = request.user))
    
    total = 0

    products = Product.objects.filter(stock__gt=1).exclude(id__in = cart_items.values('product__id'))[:2]
    print(products.query)
    for item in cart_items:
        total += item.subtotal()

    return render(request, "carrito/view.html", {'cart_items' : cart_items, 'total' : total, 'products' : products})

@login_required
def delete(request, pk):
    if request.method == "POST":
        
        cart_item = get_object_or_404(CartItem ,
                        cart__in = Cart.objects.filter(user = request.user), 
                        pk = pk
                    )
        
        cart_item.delete()
        
    return redirect(view)

@login_required
def update(request, pk):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem ,
            cart__in = Cart.objects.filter(user = request.user), 
            pk = pk
        )
        
        cart_item.quantity = request.POST['quantity']
        cart_item.save()
    
    return redirect(view)    


@login_required
def create(request, product):
    if request.method == "POST":
        product = get_object_or_404(Product ,            
            pk = product
        )

        cart, created = Cart.objects.get_or_create(          
            user=request.user,            
        )

        cart_item, created = CartItem.objects.get_or_create(
            cart = cart,
            product   = product
        )
        
        if created:
            cart_item.quantity = request.POST['quantity']
        else:
            cart_item.quantity += int(request.POST['quantity'])

        cart_item.save()
    
    return redirect(view)   






'''
class CartApi(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request):                
        CartItem.objects.filter(cart__in = Cart.objects.filter(user = request.user))
        
        return Response(response)
'''

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