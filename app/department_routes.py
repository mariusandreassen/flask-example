from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from .models import Department
from . import db

departments = Blueprint('departments', __name__)

@departments.route('/departments')
@login_required
def list_departments():
    all_departments = Department.query.all()
    return render_template('department/list.html', departments=all_departments)

@departments.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    if request.method == 'POST':
        name = request.form['name']
        if Department.query.filter_by(name=name).first():
            flash('Department already exists.')
            return redirect(url_for('departments.add_department'))

        new_department = Department(name=name)
        db.session.add(new_department)
        db.session.commit()
        flash('Department added successfully.')
        return redirect(url_for('departments.list_departments'))

    return render_template('department/add.html')

@departments.route('/departments/edit/<int:department_id>', methods=['GET', 'POST'])
@login_required
def edit_department(department_id):
    department = Department.query.get_or_404(department_id)

    if request.method == 'POST':
        department.name = request.form['name']
        db.session.commit()
        flash('Department updated successfully.')
        return redirect(url_for('departments.list_departments'))

    return render_template('department/edit.html', department=department)

@departments.route('/departments/delete/<int:department_id>')
@login_required
def delete_department(department_id):
    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()
    flash('Department deleted successfully.')
    return redirect(url_for('departments.list_departments'))