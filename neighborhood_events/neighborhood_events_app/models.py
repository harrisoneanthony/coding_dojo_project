from django.db import models
import re
import datetime as dt
from datetime import date, datetime
import bcrypt
# import pytz
# from pytz import timezone

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

timo = dt.datetime.now()
# print(timo.year)
# print(timo.month)
# print(timo.day)
# Make sure it gives the right time for Other people, because for me it gives me London Time UCT

# today = date.today() works but is on UCT time
# now_utc = datetime.now(timezone('UTC'))
# now_LA = now_utc.astimezone(timezone('America/Los_Angeles'))

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
        if (timo.year - date_of_birth.year) < 18:
            errors['dob'] = "Individuals under 18 years old cannot register"
        if timo.year - date_of_birth.year == 18:
            if timo.month < date_of_birth.month:
                errors['dob'] = "Individuals under 18 years old cannot register"
            if timo.month == date_of_birth.month:
                if timo.day < date_of_birth.day:
                    errors['dob'] = "Individuals under 18 years old cannot register"
        return errors
    # hello

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(),logged_user.password.encode()):
                errors['password'] = "Email address and password do not match records"
        else:
            errors['email'] = "Email address and password do not match records"
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
