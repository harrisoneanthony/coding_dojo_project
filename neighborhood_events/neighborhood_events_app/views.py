from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import datetime
import bcrypt

todays_date = datetime.datetime.now()

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
    user = User.objects.get(id=request.session['id'])
    context = {
        'one_user' : user,
        'user_events' : Event.objects.filter(user = User.objects.get(id=request.session['id'])),
        'todays_date' : todays_date.strftime("%a %b %d"),
        'future_events' : user.attendees.all()
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
            Event.objects.create(title = request.POST["title"], date=request.POST["date"], time=request.POST['time'], max_attendees=request.POST['max_attendees'], information=request.POST['information'], location=request.POST['location'], user = User.objects.get(id=request.session['id']), number_of_attendees=0)
            return redirect(f'join/{event.id}')
    return redirect('/dashboard')

def create_user(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/register')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name = request.POST["first_name"],last_name = request.POST["last_name"],email = request.POST["email"],dob = request.POST["dob"], password = pw_hash)
            logged_in_user = User.objects.get(email=request.POST['email'])
            request.session['id'] = logged_in_user.id
    return redirect('/dashboard')

def logout(request):
    del request.session
    return redirect('/login')

def search(request):
    context = {
        "all_events" : Event.objects.exclude(user=User.objects.get(id=request.session['id']))
    }
    return render(request, 'search.html', context)

def target_search(request):
    search = request.GET['search']
    filtered_events = Event.objects.filter(title__icontains=search)
    context = {
        "filtered_events" : filtered_events
    }
    return render(request, 'search.html', context)

def view_event(request, id):
    event = Event.objects.get(id=id)
    attendees = event.attendees.all()
    # figuring out which button to show, join or unjoin
    user_attends = False
    # figuring out if need to show event is full
    event_full = False
    attendee_list = []
    # counting attendees
    for attendee in attendees:
        attendee_list.append(attendee.first_name)
        if request.session['id'] == attendee.id:
            user_attends = True
    if event.number_of_attendees == event.max_attendees:
        event_full = True
    open_spots = event.max_attendees - event.number_of_attendees
    
    all_messages = Message.objects.filter(event=event)

    # trying not to have a trailing comma after last attendee (happens when doing a loop in HTML)
    attendee_list = ', '.join(attendee_list)
    
    context = {
        "event" : event,
        "attendees" : attendees,
        "attendee_list" : attendee_list,
        "user_attends" : user_attends,
        "event_full" : event_full,
        "open_spots" : open_spots,
        "all_messages" : all_messages,
        "user" : User.objects.get(id=request.session['id'])
    }
    return render(request, 'view_event.html', context)

def join_event(request, id):
    user = User.objects.get(id=request.session['id'])
    event = Event.objects.get(id=id)
    event.attendees.add(user)
    event.number_of_attendees += 1
    event.save()
    return redirect('/dashboard')

def unjoin_event(request, id):
    user = User.objects.get(id=request.session['id'])
    event = Event.objects.get(id=id)
    event.attendees.remove(user)
    event.number_of_attendees -= 1
    event.save()
    return redirect('/dashboard')

def cancel_event(request, id):
    user = User.objects.get(id=request.session['id'])
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('/dashboard')

def create_message(request,id):
    if request.method == "POST":
        # errors = Message.objects.message_validator(request.POST)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request,value)
        #     return redirect('/register')
        # else:
        Message.objects.create(content = request.POST["content"], user = User.objects.get(id=request.session['id']), event = Event.objects.get(id=id))
    return redirect(f'/view_event/{id}')

def delete_message(request, id, ide):
    message_to_delete = Message.objects.get(id=id)
    message_to_delete.delete()
    return redirect(f'/view_event/{ide}')

def edit_message(request, id, ide):
    event = Event.objects.get(id=ide)
    attendees = event.attendees.all()
    # figuring out which button to show, join or unjoin
    user_attends = False
    # figuring out if need to show event is full
    event_full = False
    # counting attendees
    for attendee in attendees:
        if request.session['id'] == attendee.id:
            user_attends = True
    if event.number_of_attendees == event.max_attendees:
        event_full = True
    open_spots = event.max_attendees - event.number_of_attendees
    
    all_messages = Message.objects.filter(event=event)
    edit = True

    context = {
        "event" : event,
        "attendees" : attendees,
        "user_attends" : user_attends,
        "event_full" : event_full,
        "open_spots" : open_spots,
        "all_messages" : all_messages,
        "user" : User.objects.get(id=request.session['id']),
        "editing_message" : Message.objects.get(id=id),
        "edit" : edit
    }
    return render(request, 'view_event.html', context)

def message_edited(request, id, ide):
    message = Message.objects.get(id=id)
    message.content = request.POST['content']
    message.save()
    return redirect(f'/view_event/{ide}')

def view_account(request, id):
    id = request.session['id']
    user = User.objects.get(id=id)
    context = {
        'user' : user
    }
    return render (request, 'user_profile.html', context)

def update_user(request, id):
    id = request.session['id']
    if request.method == "POST":
        user_to_update = User.objects.get(id=id)
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect(f'/account/{id}')
        else:
            user_to_update.first_name = request.POST["first_name"]
            user_to_update.last_name = request.POST["last_name"]
            user_to_update.email = request.POST["email"]
            user_to_update.dob = request.POST["dob"]
            user_to_update.password = request.POST["password"]
            user_to_update.save()
        return redirect(f'/account/{id}')
# @app.route('/run_weather', methods = ['POST'])
# def run_weather():
#     the_call = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={request.form['zipcode']}&appid=c36d1fbf846390b701c5c9f6937564e8&units=imperial").json()
#     # pprint.pprint(the_call.json())
#     # print("City",the_call['name'])
#     #need to create a session
#     session['city'] = the_call['name']
#     session['humidity'] = the_call['main']['humidity']
#     session['wind'] = the_call['wind']['speed']
#     session['temp'] = the_call['main']['temp']
#     session['description'] = the_call['weather'][0]['description']
#     # print("Description", the_call['weather'][0]['description'])
#     return redirect('/dashboard')

# Date and weather API input
#             <form action="/run_weather" method="POST">
#                 <label for="">ZIPCODE</label>
#                 <input type="text" name="zipcode">
#                 <button>Submit</button>
#             </form>
#             <h2>Current Weather Conditions:</h2>
#             <h3>City: {{session.city}}</h3>
#             <h3>Temperature: {{session.temp}} Degrees</h3>
#             <h3>Wind: {{session.wind}} MPH</h3>
#             <h3>Humidity: {{session.humidity}} %</h3>
#             <h3>Description: {{session.description}}</h3>

#   https://www.google.com/maps/embed/v1/MAP_MODE?key=YOUR_API_KEY&parameters
