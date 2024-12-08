from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Event
from database import db

event_bp = Blueprint('event', __name__)

@event_bp.route('/events')
def events():
    return render_template('events.html', events=db.get_all_events())

@event_bp.route('/events/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        event = Event(
            request.form['name'],
            request.form['date'],
            request.form['type']
        )
        db.add_event(event)
        flash('Event added successfully')
        return redirect(url_for('event.events'))
    return render_template('add_event.html')