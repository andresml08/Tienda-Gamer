from django.urls import path
from .import views

app_name ='verif_app'
urlpatterns = [
    path('Register/',views.registerUser, name ='registrar' ),
    path('Login/',views.loginUser, name ='login' ),
    path('logout/',views.logoutUser, name ='salir' ),
]