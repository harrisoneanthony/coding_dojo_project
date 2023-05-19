# Baseline Django procedure

## Create virtual environment

Mac/Linux: `python3 -m venv djangoPy3Env`  
Windows (command prompt): `python -m venv djangoPy3Env`

## Activate virtual environment

## | Mac/Linux: | `source djangoPy3Env/bin/activate`

## | Windows (command prompt): | `call djangoPy3Env\Scripts\activate`

## | Windows (git bash) : | `source djangoPy3Env/Scripts/activate`

## install Django

(djangoPy3Env) Windows/Mac:| `pip install Django==2.2.4`

 <!-- 1. With our Django virtual environment activated, create a new Django project. First navigate to where you want the project to be saved (for these first few assignments, that will be the python_stack/django/django_intro folder). Then run this command, specifying a project name of our choosing: -->

> `cd python_stack/django/django_intro`
> django_intro> `django-admin startproject your_project_name_here`

<!-- Navigate into the folder that was just created. A new Django project has just been created--let's run it! -->

django_intro> `cd your_project_name_here`
your_project_name_here> `python manage.py runserver`

<!-- 2. For every app we want to add to our project, we'll do the following: -->

your_project_name_here> `python manage.py startapp your_app_name_here`

<!-- The apps in a project CANNOT have the same name as the project. -->

<!-- 3. Let's run our app again and check it out at localhost:8000/. Whew. We've done it! -->

your_project_name_here> `python manage.py runserver`

## Configure database after updating classes in models.py

`python manage.py makemigrations`
`python manage.py migrate`

## To use the shell, we'll run the following command in our terminal from our project's root directory (where our manage.py file is located):

`python manage.py shell`

<!-- Once we're in the shell, we can access all of our functions and classes in our files. To do so, we just need to specify which modules (files) we need. Since we are interested specifically in working with our models, let's import them: -->

`from your_app_name_here.models import *`

## Overview of Commands

### Creating a new record

ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)

### Reading existing records

Methods that return a single instance of a class  
ClassName.objects.first() - gets the first record in the table  
ClassName.objects.last() - gets the last record in the table  
ClassName.objects.get(id=1) - gets the record in the table with the specified id
this method will throw an error unless only and exactly one record matches the query
Methods that return a list of instances of a class  
ClassName.objects.all() - gets all the records in the table  
ClassName.objects.filter(field1="value for field1", etc.) - gets any records matching the query provided  
ClassName.objects.exclude(field1="value for field1", etc.) - gets any records not matching the query provided

### Updating an existing record

c = ClassName.objects.get(id=1)  
c.field_name = "some new value for field_name"  
c.save()

### Deleting an existing record

c = ClassName.objects.get(id=1)  
c.delete()

### Other helpful methods

### Displaying records

ClassName.objects.get(id=1).**dict** - shows all the values of a single record as a dictionary ClassName.objects.all().values() - shows all the values of a QuerySet (i.e. multiple instances)

### Ordering records

ClassName.objects.all().order_by("field_name") - orders by field provided, ascending  
ClassName.objects.all().order_by("-field_name") - orders by field provided, descending
