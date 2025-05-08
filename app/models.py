from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255))

    users = db.relationship('User', backref='role', lazy=True)

    def __repr__(self):
        return f"<Role {self.name}>"

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"
    
class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Department {self.name}>"


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    hire_date = db.Column(db.Date)
    salary = db.Column(db.Float)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))  # Foreign key to Department
    department = db.relationship('Department', backref='employees')  # Relationship to Department

    def __repr__(self):
        return f"<Employee {self.name} - {self.position}>"

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(50))
    address = db.Column(db.String(255))

    invoices = db.relationship('Invoice', backref='customer', lazy=True)

    def __repr__(self):
        return f"<Customer {self.name}>"

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    status = db.Column(db.String(50), default='Open')

    customer = db.relationship('Customer', backref='jobs')
    assigned_to = db.relationship('Employee', backref='jobs')

    def __repr__(self):
        return f"<Job {self.title} - {self.status}>"


class LeaveRequest(db.Model):
    __tablename__ = 'leave_requests'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(255))
    status = db.Column(db.String(20), default='Pending')

    employee = db.relationship('Employee', backref='leave_requests')

    def __repr__(self):
        return f"<LeaveRequest {self.employee.name} from {self.start_date} to {self.end_date}>"


class Timesheet(db.Model):
    __tablename__ = 'timesheets'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    date = db.Column(db.Date, default=datetime.utcnow)
    hours_worked = db.Column(db.Float)
    notes = db.Column(db.String(255))

    employee = db.relationship('Employee', backref='timesheets')

    def __repr__(self):
        return f"<Timesheet {self.employee.name} - {self.hours_worked} hrs>"
    
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=True)

    tasks = db.relationship('Task', backref='project', lazy=True)
    employees = db.relationship('Employee', backref='project', lazy=True)

    def __repr__(self):
        return f"<Project {self.name}>"


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default='Not Started')
    due_date = db.Column(db.Date)

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    assigned_employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    assigned_employee = db.relationship('Employee', backref='assigned_tasks')
    def __repr__(self):
        return f"<Task {self.title}>"
    
class Invoice(db.Model):
    __tablename__ = 'invoices'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Unpaid')
    description = db.Column(db.Text)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)

    def __repr__(self):
        return f"<Invoice {self.id} - {self.amount} NOK>"