from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import Post


# Create your views here.

#function for login

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Name already in use 😁')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already in use')
        else:
            user = User.objects.create_user(username=username, email=email)
            user.set_unusable_password()
            user.save()
            return redirect('mainlogin')
    return render(request, 'register.html')


def mainlogin(request):
    if request.method == 'POST':
        username = request.POST ['username']
        email = request.POST['email']
        try:
            user = User.objects.get(username=username, email=email)
            auth_login(request, user)  # logs in the user manually
            return redirect('index')
        except User.DoesNotExist:
            messages.info(request, 'User does not exist')
            return redirect('register')
    else:
        return render(request, 'mainlogin.html')



def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts': post})