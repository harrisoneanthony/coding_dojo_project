from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name must be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name must be at least 2 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if not re.search("^(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[#$%&'()*+,-./:;<=>?@[\]^_`{|}~!]).*$", postData['password']):
            errors['password'] = "Password must be at least 8 characters and contain one number, one upper case character, and one special character."
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords must match", 'confirm_password'
        return errors
    # hello
#     hello back

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
    def __str__(self):
        return f"<Event object: {self.id} {self.title} {self.date} {self.time} {self.max_attendees} {self.information} {self.location} {self.user} >"

class Attending_event(models.Model):
    user = models.ForeignKey(User, related_name="attending_event", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="attending_event", on_delete=models.CASCADE)
    def __str__(self):
        return f"<Attending_event object: {self.id} {self.user} {self.event}>"