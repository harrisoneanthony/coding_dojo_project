from django.db import models
import re
import datetime as dt
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
time_now = dt.datetime.now()

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name must be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name must be at least 2 characters."
        all_users = User.objects.all()
        for user in all_users:
            if user.email == postData['email']:
                errors['email'] = "Email address already exists"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        # if not re.search("^(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!?]).*$", postData['password']):
        #     errors['password'] = "Password must be at least 8 characters and contain one number, one upper case character, and one special character."
        # if postData['password'] != postData['confirm_password']:
        #     errors['password'] = "Passwords must match", 'confirm_password'
        if not postData['dob']:
            errors['dob'] = "Please select a date of birth"
        date_of_birth = datetime.strptime(postData['dob'], '%Y-%m-%d')
        print(date_of_birth.year)
        if (time_now.year - date_of_birth.year) < 18:
            errors['dob'] = "Individuals under 18 years old cannot register"
        if time_now.year - date_of_birth.year == 18:
            if time_now.month < date_of_birth.month:
                errors['dob'] = "Individuals under 18 years old cannot register"
            if time_now.month == date_of_birth.month:
                if time_now.day < date_of_birth.day:
                    errors['dob'] = "Individuals under 18 years old cannot register"
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(),logged_user.password.encode()):
                errors['password'] = "Email address and password do not match our records"
        else:
            errors['email'] = "Email address and password do not match our records"
        return errors

class EventManager(models.Manager):
    def event_validator(self, postData):
        errors = {}
        if len(postData['title']) <2:
            errors['title'] = "Event title must be atleast 2 characters long."
        if not postData['date']:
            errors['date'] = "Event must have a valid date."
        if postData['time'] == None:
            errors['time'] = "Event time must be entered"
        if int(postData['max_attendees']) < 2:
            errors['max_attendees'] = "Max attendees must be atleast 2"
        if len(postData['information']) < 1:
            errors['information'] = "Event information must be entered"
        if len(postData['location']) < 1:
            errors['location'] = "Event location must be entered"
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return f"<User object: {self.id} {self.first_name} {self.last_name} {self.email} {self.password} {self.dob} >"

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    max_attendees = models.IntegerField()
    information = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EventManager()
    user = models.ForeignKey(User, related_name= "events", on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, related_name="attendees")
    def __str__(self):
        return f"<Event object: {self.id} {self.title} {self.date} {self.time} {self.max_attendees} {self.information} {self.location} {self.user} >"

    

# API Key
# AIzaSyDyZWSyzkDoh8tieaORQh_iXNMSpwuADVM
