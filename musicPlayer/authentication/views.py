from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def UserRegister(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
    
        if form.is_valid():
            form.save()
            messages.success(request, "Register Successfully")
            return redirect('login')
    else:
        form = UserRegisterForm()
           
    return render(request, "authentication/register.html", {'form': form})


def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Login Successfully")
                return redirect('music')
            else:
                messages.error(request, "User is not active")
        else:
            messages.error(request, "Username or password invalid")
    
    return render(request, "authentication/login.html")


def UserLogout(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('login')