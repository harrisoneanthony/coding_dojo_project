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
        # if len(postData['password']) < 8:
        #     errors['password'] = "Password must be at least 8 characters."
        # if not re.search("[A-Z]", postData['password']):
        #     errors['password'] = "Password must contain at least one capital letter."
        # if not re.search("[0-9]", postData['password']):
            # errors['password'] = "Password must contain at least one number."
        if not re.search("^(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", postData['password']):
            errors['password'] = "Password must be at least 8 characters and contain one number, one upper case character, and one special character."
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords must match", 'confirm_password'
        return errors
    # hello
#     hello back


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
