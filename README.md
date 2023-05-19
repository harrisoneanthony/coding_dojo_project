# Baseline Django procedure

## Create virtual environment

| Mac/Linux: | `python3 -m venv djangoPy3Env`
-------------+----------------------------------------------------
| Windows (command prompt): | `python -m venv djangoPy3Env`

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
