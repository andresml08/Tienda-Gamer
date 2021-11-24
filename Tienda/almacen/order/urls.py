from django.urls import path
from . import views 
# from django.contrib.auth.decorators import login_required

app_name = 'order_app'

urlpatterns = [
path('Process_order/',views.process_order, name='order'),
path('Pedidos/',views.OrderList.as_view(), name='pedidos'),
path('Detalle/<pk>/',views.OrderDetail, name='detalle'),
path('Eliminar/<pk>/',views.eliminarView.as_view(), name='eliminar'),
path('editar/<pk>/',views.EditarView.as_view(), name='editar'),
]