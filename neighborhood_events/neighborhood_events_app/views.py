from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def login_user(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/login')
    logged_in_user = User.objects.get(email=request.POST['email'])
    request.session['id'] = logged_in_user.id
    return redirect('/dashboard')

def dashboard(request):
    context = {
        'one_user' : User.objects.get(id=request.session['id'])
    }
    return render(request, "dashboard.html", context)

def create_user(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/register')
        else:
            # creating the hash before feeding it into the User class
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            User.objects.create(first_name = request.POST["first_name"],last_name = request.POST["last_name"],email = request.POST["email"],dob = request.POST["dob"], password = pw_hash)
            logged_in_user = User.objects.get(email=request.POST['email'])
            request.session['id'] = logged_in_user.id
    return redirect('/dashboard')

def logout(request):
    del request.session
    return redirect('/login')
