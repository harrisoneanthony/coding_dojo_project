from flask_app import app
from flask_app.controllers import users_controllers
# from flask_app.controllers import paintings_controllers
from flask_app.models.users_models import User
from flask_app.models.events_models import Event

if __name__ == "__main__":
    app.run(debug = True, port=5001)