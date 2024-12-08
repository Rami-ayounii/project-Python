from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
import calendar
from models import Event
from database import db

bp = Blueprint('events', __name__)

@bp.route('/calendar')
def view_calendar():
    now = datetime.now()
    cal = calendar.monthcalendar(now.year, now.month)
    return render_template('calendar.html',
                         calendar=cal,
                         events=db.get_all_events(),
                         current_month=now.month,
                         current_year=now.year)

@bp.route('/events/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        event = Event(
            name=request.form['event_name'],
            date=request.form['event_date'],
            event_type=request.form['event_type']
        )
        db.add_event(event)
        flash('Event added successfully!')
        return redirect(url_for('events.view_calendar'))
    return render_template('add_event.html')