from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CollectionCenter(models.Model):
    user              = models.OneToOneField(User, verbose_name=_("Usuario"), on_delete=models.CASCADE, related_name='collection_center')
    name              = models.CharField(max_length=60)
    description       = models.CharField(max_length=255)
    address           = models.CharField(max_length=255)
    image             = models.CharField(max_length=255,default="")
    latitude          = models.CharField(max_length=60)
    longitude         = models.CharField(max_length=60)
    times_visited     = models.PositiveSmallIntegerField()
    status            = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    estatus = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    edicion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creacion"]

    def __str__(self):
        return self.nombre


    

class Product(models.Model):
    STATUS = (
        (0, _('Inactivo')),
        (1, _('Activo') ),
    )

    CONDITIONS = (
        (0, _('Nuevo')),
        (1, _('Usado'))
    )

    TYPES = (
        (0, 'Producto'),
        (1, 'Servicio'),
        (2, 'Medicina'),
    )

    name              = models.CharField(max_length=60)
    description       = models.CharField(max_length=255)
    image             = models.CharField(max_length=255,default="")
    price             = models.DecimalField( max_digits=7, decimal_places=2)
    donated           = models.BooleanField(default=True)
    collection_center = models.ForeignKey(CollectionCenter, null=False, blank=False, on_delete=models.CASCADE)
    category          = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    type_product      = models.PositiveSmallIntegerField( choices=TYPES)
    condition         = models.PositiveSmallIntegerField(choices=CONDITIONS)
    stock             = models.PositiveIntegerField()
    created_at        = models.DateField( auto_now=False, auto_now_add=True)
    status            = models.PositiveSmallIntegerField(choices=STATUS)

    def Name(self):
        return '{0} $ {1}'.format(self.name, self.price)

    def statusText(self):
        return self.STATUS[self.status][1]
    
    def typeText(self):
        return self.TYPES[self.type_product][1]
    
    def conditionText(self):
        return self.CONDITIONS[self.condition][1]

        

    def __str__(self):
        return self.Name()

class Order(models.Model):  
    STATUS = (
        (0, _('Cancelado')),
        (1, _('Pendiente') ),
        (2, _('Entregado') ),
    )  
    user              = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    collection_center = models.ForeignKey(CollectionCenter, null=False, blank=False, on_delete=models.CASCADE)
    status            = models.PositiveSmallIntegerField()
    date_at           = models.DateField( auto_now=False, auto_now_add=False)
    created_at        = models.DateTimeField( auto_now=False, auto_now_add=True)

    def statusText(self):
        return self.STATUS[self.status][1]

    def __str__(self):
        return '{0} - date: {1}'.format(self.id, self.date_at)  

class OrderDetail(models.Model):
    order   = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE)
    name    = models.CharField(max_length=100)
    donated = models.BooleanField(default=True)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    price   = models.DecimalField( max_digits=9, decimal_places=2)
    qty     = models.PositiveIntegerField()

    def __str__(self):
        return 'Order: {0} - prd: {1} - price: {2} - qty : {3} - donated : {4}'.format(self.order, self.name, self.price, self.qty, self.donated)  

class Slider(models.Model):
    name              = models.CharField(max_length=60)
    description       = models.CharField(max_length=255)
    description_detail= models.CharField(max_length=255)
    image             = models.CharField(max_length=255,default="")
    status            = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name




