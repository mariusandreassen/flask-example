import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 





app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', 'dev.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50))
    hire_date = db.Column(db.Date)
    salary = db.Column(db.Float)

    def __repr__(self):
        return f"<Employee {self.name} - {self.position}>"

@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
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
            hire_date=hire_date if hire_date else None,
            salary=float(salary) if salary else None
        )
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
