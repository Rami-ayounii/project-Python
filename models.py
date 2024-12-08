from datetime import datetime

class Employee:
    def __init__(self, first_name, last_name, position, department, hire_date):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.department = department
        self.hire_date = hire_date
        self.reviews = []

class Event:
    def __init__(self, name, date, event_type):
        self.name = name
        self.date = date
        self.type = event_type

class PerformenceReview:
    def __init__(self, date, score, feedback):
        self.date = date
        self.score = score
        self.feedback = feedback