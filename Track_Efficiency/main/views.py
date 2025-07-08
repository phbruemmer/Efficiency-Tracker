from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import make_password


"""
### IMPORTANT ###

This small project is just a temporary solution.
I needed this fast.
I will work on a completely new and better version soon.
The new version will appear in a new repository on GitHub.

"""


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register_view')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register_view')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('register_view')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully.")
        return redirect('tracker_view')
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tracker_view')
        else:
            pass
            # messages.error(request, 'Invalid username or password')
    return render(request, "login.html")


def tracker_view(request):
    return render(request, "tracker.html")

