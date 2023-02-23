from flask import render_template,redirect,request,session
from flask import flash
from flask_app import app
from flask_app.models.users_models import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('register.html')