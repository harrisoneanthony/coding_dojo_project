from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def login_user(request):
    logged_in_user = User.objects.get(email=request.POST['email'])
    request.session['id'] = logged_in_user.id
    return redirect('/dashboard')

def dashboard(request):
    context = {
        'one_user' : User.objects.get(id=request.session['id'])
    }
    return render(request, "dashboard.html", context)

def create_event_page(request):
    return render(request, "create_event.html")

def create_event(request):
    if request.method == "POST":
        errors = Event.objects.event_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/create/event')
        else:
            Event.objects.create(title = request.POST["title"], date=request.POST["date"], time=request.POST['time'], max_attendees=request.POST['max_attendees'], information=request.POST['information'], location=request.POST['location'])

def create_user(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/register')
        else:
            User.objects.create(first_name = request.POST["first_name"],last_name = request.POST["last_name"],email = request.POST["email"],dob = request.POST["dob"], password = request.POST["password"])
    return redirect('/dashboard')

def logout(request):
    del request.session
    return redirect('/login')
