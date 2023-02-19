from django.shortcuts import render, redirect
from .models import *

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def login_user(request):
    pass

def dashboard(request, id):
    context = {
        "id" : id
    }
    return render(request, "dashboard.html", context)

def create_user(request):
    if request.method == "POST":
        User.objects.create(first_name = request.POST["first_name"],last_name = request.POST["last_name"],email = request.POST["email"],dob = request.POST["dob"], password = request.POST["password"])
    return redirect('/dashboard')

def logout(request):
    del request.session
    return redirect('/login')
