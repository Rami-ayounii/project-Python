from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Employee
from database import db

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employees')
def employees():
    return render_template('employees.html', employees=db.get_all_employees())

@employee_bp.route('/employees/add', methods=['GET', 'POST'])
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
        return redirect(url_for('employee.employees'))
    return render_template('add_employee.html')