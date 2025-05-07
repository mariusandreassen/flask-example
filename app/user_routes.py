from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from .models import User, Role
from . import db

users = Blueprint('users', __name__)

@users.route('/users')
@login_required
def list_users():
    all_users = User.query.all()
    return render_template('users/list.html', users=all_users)

@users.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    roles = Role.query.all()

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.role_id = request.form['role_id']
        db.session.commit()
        flash('User updated successfully.')
        return redirect(url_for('users.list_users'))

    return render_template('users/edit.html', user=user, roles=roles)

@users.route('/users/delete/<int:user_id>')
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully.')
    return redirect(url_for('users.list_users'))