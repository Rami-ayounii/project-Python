class Database:
    def __init__(self):
        self.employees = []
        self.events = []
        self.reviews = []

    def add_employee(self, employee):
        employee.id = len(self.employees) + 1
        self.employees.append(employee)
        return employee

    def get_employee(self, employee_id):
        return next((emp for emp in self.employees if emp.id == employee_id), None)

    def get_all_employees(self):
        return self.employees

    def add_event(self, event):
        self.events.append(event)
        return event

    def get_all_events(self):
        return self.events
    
    def add_performance_review(self, employee_id,review):
        employee = self.get_employee(employee_id)
        if employee:
            employee.reviews.append(review)
            return True
        return False

db = Database()