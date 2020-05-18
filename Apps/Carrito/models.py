from django.db import models
from Apps.Web.models import Product
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return str(self.cart)
        except:
            return self.product.name
    def subtotal(self):
        return float(self.quantity)*float(self.product.price)

class Cart(models.Model):
    id      = models.AutoField(primary_key=True)
    user    = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total   = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    active  = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cart id: %s, Client: %s" %(self.id, self.user)
    