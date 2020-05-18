from django import forms
from django.forms import ModelForm
from Apps.Web.models import Cliente, Product, CollectionCenter


class ClienteForm(ModelForm):
    nombre  = forms.CharField(min_length=2, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))
    contrasenia = forms.CharField(min_length=6, max_length=8, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Contraseña'}))
    apellido  = forms.CharField(min_length=2, max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellidos'}))
    email  = forms.CharField(min_length=6, max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'contrasenia']

class ProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)        
        self.fields['collection_center'].initial = 1
    
    class Meta:
        model = Product
        
        labels = {
            'name': _('Nombre'),
        }
        
        widgets= {'collection_center': forms.HiddenInput()}
        fields = "__all__"