from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def signin(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username = username).exists():
            error_message = "Username Already Exists"
        
        else:
            user = User.objects.create_user(username=username , password=password)  
            return redirect('login')  
    return render(request ,'auth/signin.html', {'error_message':error_message})


def login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = "Username or Password is incorrect"  


    return render(request,'auth/login.html', {'error_message': error_message})


def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')