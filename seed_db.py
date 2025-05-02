from app import db, Employee, app
from datetime import date

with app.app_context():
    db.create_all()

    emp = Employee(
        name="Alice DevOps",
        position="Site Reliability Engineer",
        department="IT",
        hire_date=date(2023, 5, 1),
        salary=75000
    )

    db.session.add(emp)
    db.session.commit()

    print(Employee.query.all())
