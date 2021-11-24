from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import ProdForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
# Create your views here.
from .carrito import Carrito
from .models import Producto


def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})


def CarritoView(request):
    productos = Producto.objects.all()
    return render(request, "carrito.html", {'productos':productos})


@login_required(login_url='/Accounts/Login')
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("prod_app:carrito")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("prod_app:carrito")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("prod_app:carrito")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("prod_app:carrito")


class indexView(TemplateView):
    template_name = "index.html"
    

class RegistrarprodView(CreateView):
    template_name = "productos/prod.html"
    model = Producto
    form_class = ProdForm
    success_url = reverse_lazy('prod_app:index')
    
    def form_valid(self, form):
        #logica del proceso
        print(self)
        return super(RegistrarprodView, self).form_valid(form)
    

class editarProdUpdateView(UpdateView):
    template_name = "productos/editprod.html"
    model = Producto
    form_class = ProdForm
    success_url = reverse_lazy('prod_app:selectprod')
    
    def post(self, request, *args: str, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super(editarProdUpdateView, self).form_valid(form)
    

class prodDeleteView(DeleteView):
    template_name = "productos/borrarprod.html"
    model = Producto
    success_url = reverse_lazy('prod_app:listaprod')
    


# class SelectView(TemplateView):
#     template_name = "productos/selectprod.html"
@login_required(login_url='/Accounts/Login')
def SelectView(request):
    productos = Producto.objects.all()
    return render(request, "productos/selectprod.html", {'productos':productos})
    
    
class inicioproductosListView(ListView):
    model = Producto
    template_name = "productos/listaprod.html"
    context_object_name = 'products'
    ordering = ['id']
    
class facturaListView(ListView):
    model = Producto
    template_name = "factura.html"
    context_object_name = 'facture'
    success_url = reverse_lazy('prod_app:tienda.html')

@login_required(login_url='/Accounts/Login')
def facturaView(request):
    productos = Producto.objects.all()
    return render(request, "factura.html", {'productos':productos})