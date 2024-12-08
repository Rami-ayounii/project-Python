from flask import Blueprint
from .employee_routes import employee_bp
from .event_routes import event_bp
from .review_routes import review_bp

def register_routes(app):
    app.register_blueprint(employee_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(review_bp)