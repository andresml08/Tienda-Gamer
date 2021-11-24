from django.urls import path
from . import views 

app_name = 'prod_app'

urlpatterns = [
    path('', views.indexView.as_view(), name="index"),
    path('RegistrarProd/',views.RegistrarprodView.as_view(), name='regprod'),
    path('EditarProd/<pk>/',views.editarProdUpdateView.as_view(), name='editprod'),
    path('DeleteProd/<pk>/',views.prodDeleteView.as_view(), name='deleteprod'),
    path('Selectprod/',views.SelectView, name='selectprod'),
    path('ListaProd/',views.inicioproductosListView.as_view(), name='listaprod'),
    path('Compras/', views.tienda, name="Tienda"),
    path('Carrito/',views.CarritoView, name='carrito'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('Factura/',views.facturaView, name='facturaprod'),
]