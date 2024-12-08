from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Employee
from database import db

bp = Blueprint('employees', __name__)

@bp.route('/employees')
def list_employees():
    return render_template('employees.html', employees=db.get_all_employees())

@bp.route('/employees/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        employee = Employee(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            position=request.form['position'],
            department=request.form['department'],
            hire_date=request.form['hire_date']
        )
        db.add_employee(employee)
        flash('Employee added successfully!')
        return redirect(url_for('employees.list_employees'))
    return render_template('add_employee.html')