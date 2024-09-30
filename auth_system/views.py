from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']
        if p1 == p2: 
            if User.objects.filter(username = username).exists():
                context = {
                    'error': "USERNAME ALREADY EXITS"
                }
                return render(request, 'signup.html', context)
            else:
                User.objects.create_user(
                    username = username,
                    password = p1
                )
                return redirect('login')
    return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        p = request.POST['password']

        user = authenticate(request, username = username, password = p)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return render(request, 'login.html')

