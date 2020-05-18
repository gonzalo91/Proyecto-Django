from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from Apps.Web.forms import ProductForm
from Apps.Web.models import *
from django.views.generic import ListView, DetailView
from datetime import date
from django.db import connection
#from django.conf import settings
#from django.contrib import messages
from django.db import models
from .Services.Home import Home
#from Apps.Web.models import Order
#from .forms import ClienteForm

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import IsUserRecolector
from .decorators import user_has_c_c_and_is_recolector


class HomeApi(APIView):
    permission_classes = [IsUserRecolector]
    def get(self, request):        
        home = Home(request.user.collection_center.id)
        response = home.all()
        return Response(response)

@login_required
@user_passes_test(user_has_c_c_and_is_recolector)
def home(request):
    return render(request, 'home/index.html')

    

class IndexView(ListView):
    template_name='products/index.html'
    context_object_name = 'product_list'    
    paginate_by = 10    
    def get_queryset(self):        
        return Product.objects.filter(collection_center=self.request.user.collection_center).order_by('name')


class ClientView(ListView):
    template_name = "clients/index.html"
    context_object_name = 'client_list'
    paginate_by = 10    
    def get_queryset(self):                         
        return User.objects.select_related('collection_center').filter(id__in=Order.objects.filter( collection_center= self.request.user.collection_center ).values_list('user'))

class OrderView(ListView):
    template_name = "orders/index.html"
    context_object_name = 'order_list'
    paginate_by = 10    
    def get_queryset(self):                         
        return Order.objects.select_related('user').filter( collection_center= self.request.user.collection_center ).order_by('created_at')

@user_passes_test(user_has_c_c_and_is_recolector)
def order_view(request, pk, template_name='orders/detail.html'):    
    order = get_object_or_404(Order, pk=pk, collection_center = request.user.collection_center.id)                
    order_details = OrderDetail.objects.filter(order = order)

    extras = {
        'donated' : 0,
        'sold'    : 0,
        'amount'  : 0
    }
    
    for order_detail in order_details:
        extras['amount'] += order_detail.price * order_detail.qty
        if order_detail.donated:
            extras['donated'] += 1
        else:
            extras['sold'] += 1
            
    return render(request, template_name, {'order' : order, 'order_details' : order_details, 'extras' : extras})
        
    
    

@user_passes_test(user_has_c_c_and_is_recolector)
def productview(request):

    if request.method == 'POST':

        cpPost = request.POST.copy()        
        cpPost['collection_center'] = request.user.collection_center.id
        
        form = ProductForm(cpPost)     
                
        if form.is_valid():
            form.save()                                                  
            return redirect('product_index')        
        
    form = ProductForm()    
    return render(request,'products/new.html',{'form': form})  

@user_passes_test(user_has_c_c_and_is_recolector)
def product_edit(request, pk, template_name='products/detail.html'):    
    
    product = get_object_or_404(Product, pk=pk, collection_center = request.user.collection_center.id)
    
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()        
    
    return render(request, template_name, {'form':form, 'product' : product})

@user_passes_test(user_has_c_c_and_is_recolector)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)    
    if request.method=='POST':
        product.delete()
        return redirect('product_index')
    return redirect('product_index')

@user_passes_test(user_has_c_c_and_is_recolector)
def action_order(request):
    if request.method == 'POST':        
        statusTo = 2 if request.POST['action'] == 'confirm' else 0
        order_id = request.POST['order_id']
        order = get_object_or_404(Order, pk=order_id)
        order.status = statusTo
        
        if order.save():
            return JsonResponse({'status' : 'ok'})   

    return JsonResponse({'status' : 'none'})

'''
def home_api(request):
    home = Home()    
    response = home.all()

    return JsonResponse(response)








    

  

def edit(request, pk, template_name='admin/products/detail.html'):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()        
    
    return render(request, template_name, {'form':form, 'product' : product})




# Create your views here.
def admini(request):
    if request.session.has_key('admin_is_logged'):
        return render(request, 'administracion/index.html')
    return redirect('ingresar')

def login(request):
    if request.session.has_key('admin_is_logged'):
        return redirect('administrador')

    if request.POST:
        email = request.POST['correo']
        contrasenia = request.POST['contraseña']
        count = Usuario.objects.filter(email=email, contrasenia=contrasenia, perfil=1).count()
        if count > 0:
            request.session['admin_is_logged'] = True
            usuario = Usuario.objects.get(email=email, contrasenia=contrasenia, perfil=1)
            request.session['admin_name'] = usuario.nombre + " " + usuario.apellido
            request.session['admin_image'] = settings.MEDIA_URL + str(usuario.imagen)
            return redirect('administrador')
        else:
            messages.error(request, 'correo o contraseña invalidos')
            return redirect('ingresar') 
    return render(request, 'administracion/login.html')

def salir(request):
    del request.session['admin_is_logged']
    return redirect('ingresar')

def categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias':categorias
    }
    return render(request, 'administracion/categorias.html', context)

def categoria_detalle(request, id):
    categoria=Categoria.objects.get(id=id)
    context={
        'categoria':categoria,
        'desicion':True
    }
    return render(request, 'administracion/categorias-detalle.html', context)

def actualizarCategoria(request, id):
    nombre = request.POST['categoria']
    if 'estatus' in request.POST:
        estatus = 1
    else:
        estatus = 0
    Categoria.objects.filter(id=id).update(nombre=nombre, estatus=estatus)
    return redirect('categorias')

def eliminarCategoria(request, id):
    Categoria.objects.filter(id=id).delete()
    return redirect('categorias')

def categoria_detalle2(request):
    #categoria=Categoria(nombre=nombre, estatus=estatus)
    #categoria.save()
    categoria=''
    context={
        'categoria':categoria,
        'desicion':False
    }
    return render(request, 'administracion/categorias-detalle.html', context)

    
def crearCategoria(request):
    nombre = request.POST['categoria']
    if 'estatus' in request.POST:
        estatus = 1
    else:
        estatus = 0
    categoria=Categoria(nombre=nombre, estatus=estatus)
    categoria.save()
    return redirect('categorias')
    
def usuario(request):
    usuarios = Usuario.objects.all()
    context = {
        'usuarios':usuarios
    }
    return render(request, 'administracion/usuarios.html', context)

def usuario_detalle(request, id=0):
    context = {}
    if id > 0:
        usuario = Usuario.objects.get(id=id)
        context={
            'usuario':usuario,
        }
    return render(request, 'administracion/usuarios-detalle.html', context)

def crud_usuario(request, id=0):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    contrasenia = request.POST['contrasenia']
    imagen = request.FILES.get('imagen')
    perfil = 1 if 'perfil' in request.POST else 0
    estatus = 1 if 'estatus' in request.POST else 0
    if int(request.POST['accion']) == 0:#Opcion para crear nuevo usuario
        usuario = Usuario(nombre=nombre, apellido=apellido, email=email, contrasenia=contrasenia, imagen=imagen, perfil=perfil, estatus=estatus)
        usuario.save()
    elif int(request.POST['accion']) == 1:#Opcion para editar nuevo usuario
        Usuario.objects.filter(id=id).update(nombre=nombre, apellido=apellido, email=email, contrasenia=contrasenia, perfil=perfil, estatus=estatus)
        if imagen:
            Usuario.objects.get(id=id).imagen.delete(save=True)
            usuario = Usuario.objects.get(id=id)
            usuario.imagen=imagen
            usuario.save()
    return redirect('usuarios')

def eliminar_usuario(request, id):
    if Usuario.objects.get(id=id).imagen:
        Usuario.objects.get(id=id).imagen.delete(save=True)
    Usuario.objects.get(id=id).delete()
    return redirect('usuarios')

def clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes':clientes
    }
    return render(request, 'administracion/clientes.html', context)

def registro(request):
    if request.session.has_key('client_is_logged'):
        return redirect('index')
    context = {
        'formulario':ClienteForm()
    }
    if request.POST:
        contraseña = request.POST['contrasenia']
        contraseña2 = request.POST['contrasenia2']
        if contraseña == contraseña2:
            formulario = ClienteForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, 'Registro Exitoso, Ahora puedes iniciar Sesión')
                return redirect('registro')
        else:
            messages.error(request, 'Contraseñas no coinciden, intentelo de nuevo')
            return redirect('registro')
    return render(request, 'web/registro.html', context)

def login_cl(request):
    if request.session.has_key('client_is_logged'):
        return redirect('index')
    if request.POST:
        email = request.POST['correo']
        contrasenia = request.POST['contraseña']
        count = Cliente.objects.filter(email=email, contrasenia=contrasenia).count()
        if count > 0:
            request.session['client_is_logged'] = True
            cliente = Cliente.objects.get(email=email, contrasenia=contrasenia)
            request.session['client_name'] = cliente.nombre + " " + cliente.apellido
            request.session['client_image'] = settings.MEDIA_URL + str(cliente.imagen)
            return redirect('index')
        else:
            messages.error(request, 'correo o contraseña invalidos')
            return redirect('login') 
    return render(request, 'web/login.html')

def logout(request):
    if 'client_is_logged' in request.session: del request.session['client_is_logged']
    if 'client_name' in request.session: del request.session['client_name']
    if 'client_image' in request.session: del request.session['client_image']
    return redirect('index')

def index(request):
    if request.session.has_key('client_is_logged'):
        return render(request, 'web/index.html')
    return render(request, 'web/index.html')



'''


