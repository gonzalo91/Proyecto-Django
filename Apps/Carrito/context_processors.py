


def cart(request):
    from .models import Cart, CartItem
    cart_items_test = []

    if(request.user.is_authenticated):
        cart_items_test = CartItem.objects.filter(cart__in = Cart.objects.filter(user = request.user))
    
    return { 'cart_items' : cart_items_test }

    