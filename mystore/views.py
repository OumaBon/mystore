from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegistrationForm 
from .models import UserRole 

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name':'Joan'})


def about(request):
    return render(request, 'about.html', {})



def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            UserRole.objects.create(user=user, role=role)
            login(request, user)
            return redirect('home')
        else:
            form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('login') 
