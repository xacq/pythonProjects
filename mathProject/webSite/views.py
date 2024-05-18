from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
def index (request):
    return render(request, 'index.html')


@login_required(login_url='login')
def HomePage(request):
    username = request.session.get('username', None)
    if username:
        context = {'username': username}
        return render(request, 'home.html', context)
    else:
        return HttpResponse("Debe iniciar sesión primero.")
    
    
@login_required(login_url='login')
def Edit(request):
    username = request.session.get('username', None)
    if username:
        context = {'username': username}
        return render(request, 'edit.html', context)
    else:
        return HttpResponse("Debe iniciar sesión primero.")
    

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Las contraseñas no coinciden!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            request.session['username'] = username
            return redirect('home')
        else:
            return HttpResponse ("Usuario y Contraseña incorrectos!!!")
    return render (request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('index')
