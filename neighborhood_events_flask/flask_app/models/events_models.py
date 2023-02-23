from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'neighborhood_events_flask_app'

class Event:
    def __init__(self,data):
        self.id = data['id'],
        self.title = data['title'],
        self.date = data['date'],
        self.time = data['time'],
        self.information = data['information'],
        self.location = data['location'],
        self.max_attendees = data['max_attendees'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_event(event):
        is_valid = True
        if len(event['title']) == 0 or len(event['information']) == 0 or event['date']==None or event['time']==None or len(event['location']) == 0 or event['max_attendees'] == 0:
            flash("All fields required")
            is_valid = False
        if len(event['title']) < 2:
            flash("Event title must be at least 2 characters.")
            is_valid = False
        if event['date'] == None:
            flash("Date is required.")
            is_valid = False
        if event['time'] == None:
            flash("Event time is required")
            is_valid = False
        if len(event['information']) < 1:
            flash("Event information is required")
            is_valid = False
        if int(event['max_attendees']) < 2:
            flash("Event requires at least 2 attendee spots")
            is_valid = False
        return is_valid