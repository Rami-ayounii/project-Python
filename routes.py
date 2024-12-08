from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Employee, Event, Review
from database import db

def register_routes(app):
    @app.route('/employees')
    def employees():
        return render_template('employees.html', employees=db.get_all_employees())

    @app.route('/employees/add', methods=['GET', 'POST'])
    def add_employee():
        if request.method == 'POST':
            employee = Employee(
                request.form['first_name'],
                request.form['last_name'],
                request.form['position'],
                request.form['department'],
                request.form['hire_date']
            )
            db.add_employee(employee)
            flash('Employee added successfully')
            return redirect(url_for('employees'))
        return render_template('add_employee.html')

    @app.route('/events')
    def events():
        return render_template('events.html', events=db.get_all_events())

    @app.route('/events/add', methods=['GET', 'POST'])
    def add_event():
        if request.method == 'POST':
            event = Event(
                request.form['name'],
                request.form['date'],
                request.form['type']
            )
            db.add_event(event)
            flash('Event added successfully')
            return redirect(url_for('events'))
        return render_template('add_event.html')

    @app.route('/reviews')
    def reviews():
        return render_template('reviews.html', employees=db.get_all_employees())

    @app.route('/reviews/add', methods=['GET', 'POST'])
    def add_review():
        if request.method == 'POST':
            review = Review(
                request.form['date'],
                int(request.form['score']),
                request.form['feedback']
            )
            db.add_review(int(request.form['employee_id']), review)
            flash('Review added successfully')
            return redirect(url_for('reviews'))
        return render_template('add_review.html', employees=db.get_all_employees())