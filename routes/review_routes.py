from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import PerformanceReview
from database import db

review_bp = Blueprint('review', __name__)

@review_bp.route('/reviews')
def reviews():
    return render_template('reviews.html', employees=db.get_all_employees())

@review_bp.route('/reviews/add', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        review = PerformanceReview(
            request.form['date'],
            int(request.form['score']),
            request.form['feedback']
        )
        db.add_performance_review(int(request.form['employee_id']),review)
        flash('Review added successfully')
        print(review)
        return redirect(url_for('review.reviews'))
    return render_template('add_review.html', employees=db.get_all_employees())