from django.shortcuts import redirect, render
from .forms import RegisterForm
from django. contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def registerUser(request):
    form = RegisterForm()
    if  request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verif_app:login')
    else :
        form = RegisterForm()
    return render(request, 'autenticacion/register.html',{'form':form})
  

def loginUser(request):
    if  request.method =='POST':
        username =request.POST.get('username')
        password =request.POST.get("password")
      
        if username and password:
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('prod_app:index')
            else :
                messages.error(request, 'username or password is incorrect')
        else :
            messages.error(request, 'Fill out all the fields')

    return render (request, 'autenticacion/login.html',{})


def logoutUser(request):
    logout(request)
    return redirect('prod_app:index')