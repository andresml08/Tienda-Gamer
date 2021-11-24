from django.contrib.auth.models import User
# from django.db.models.expressions import F,Sum
from django.http import request
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
from django.views.generic import DetailView,UpdateView,DeleteView
from django.views.generic.list import ListView

from mercancia.models import Producto

from .forms import estadoForm
from .models import Order, OrderLine
from mercancia.carrito import Carrito
# Create your views here.

@login_required(login_url='/Accounts/Login')
def process_order(request):
    order = Order.objects.create(user=request.user, completed=True)
    carrito = Carrito(request)
    order_lines = list()
    for key, value in carrito.carrito.items():
        order_lines.append(
            OrderLine(
                product_id=key,
                cantidad=value["cantidad"],
                user=request.user,
                order=order,
            )
        )
    OrderLine.objects.bulk_create(order_lines)
    
    send_order_email(    
    order=order,
    order_lines=order_lines,
    username=request.user.username,
    user_email=request.user.email,
    )
    
    carrito.limpiar()
    
    messages.success(request, "EL pedido se ha creado correctamente!")
    return redirect("prod_app:Tienda")

def send_order_email(**kwargs):
    subject = "Gracias por tu pedido"
    html_message = render_to_string("emails/nuevo_pedido.html", {
        "order": kwargs.get("order"),
        "order_lines": kwargs.get("order_lines"),
        "username": kwargs.get("username")
    })
    
    plain_message = strip_tags(html_message)
    from_email = "joseelblanco13@gmail.com"
    to = kwargs.get("user_email")
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    
class OrderList(ListView):
    model = Order
    ordering = ["-id"]
    template_name = "orders/pedidos.html"
    # context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        # print(queryset).
        print(self.request.user.is_superuser)
        if self.request.user.is_superuser:
            return queryset.all()
        else:
            return queryset.filter(user=self.request.user)
    
    
def OrderDetail(request,pk):
    total = 0
    detalles =  OrderLine.objects.raw('select o.id,oo.id,m.id, marca, modelo, precio,cantidad, cantidad*precio as total from orders o left join order_orderline oo on oo.order_id = o.id left join mercancia_producto as m on oo.product_id = m.id where o.id = %s', [pk])
    for detalle in detalles:
        total +=detalle.total  
    return render(request,'orders/detalle.html',{'datos':detalles,'total':total})  


class EditarView(UpdateView):
    template_name = "orders/editar.html"
    model = Order
    form_class = estadoForm
    success_url = reverse_lazy('order_app:pedidos')
    
    def post(self, request, *args: str, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        return super(EditarView, self).form_valid(form)


class eliminarView(DeleteView):
    template_name = "orders/eliminarp.html"
    model = Order
    success_url = reverse_lazy('order_app:pedidos')
  
