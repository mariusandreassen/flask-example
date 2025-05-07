from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from .models import Employee
from . import db

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@routes.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        department = request.form.get('department')
        hire_date_raw = request.form.get('hire_date')
        hire_date = datetime.strptime(hire_date_raw, '%Y-%m-%d').date() if hire_date_raw else None
        salary = request.form.get('salary')

        new_employee = Employee(
            name=name,
            position=position,
            department=department,
            hire_date=hire_date,
            salary=float(salary) if salary else None
        )
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('routes.index'))

    return render_template('add.html')
@routes.route('/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)

    if request.method == 'POST':
        employee.name = request.form['name']
        employee.position = request.form['position']
        employee.department = request.form.get('department')
        hire_date_raw = request.form.get('hire_date')
        employee.hire_date = datetime.strptime(hire_date_raw, '%Y-%m-%d').date() if hire_date_raw else None
        employee.salary = float(request.form.get('salary')) if request.form.get('salary') else None

        db.session.commit()
        flash('Employee updated successfully.')
        return redirect(url_for('routes.index'))

    return render_template('routes/edit.html', employee=employee)

@routes.route('/delete/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee deleted.')
    return redirect(url_for('routes.index'))