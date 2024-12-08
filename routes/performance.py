from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import PerformanceReview
from database import db

bp = Blueprint('performance', __name__)

@bp.route('/performance')
def performance():
    return render_template('performance.html', employees=db.get_all_employees())

@bp.route('/performance/add', methods=['GET', 'POST'])
def add_performance():
    if request.method == 'POST':
        employee_id = int(request.form['employee_id'])
        review = PerformanceReview(
            date=request.form['date'],
            score=int(request.form['score']),
            feedback=request.form['feedback']
        )
        if db.add_performance_review(employee_id, review):
            flash('Performance evaluation added successfully!')
            return redirect(url_for('performance.performance'))
    return render_template('add_performance.html', employees=db.get_all_employees())