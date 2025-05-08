def seed_database(db, Employee, Department, User):
    """Seed the database with initial sample data if empty."""
    if not Employee.query.first():
        # Ensure the department exists or create it
        management_department = (
            Department.query.filter_by(name="Management").first()
            or Department(name="Management")
        )
        if management_department.id is None:
            db.session.add(management_department)
            db.session.commit()

        # Add sample employees by foreign key
        sample_employees = [
            Employee(
                name="Hennig Olsen",
                position="CEO",
                department_id=management_department.id,
                hire_date=None,
                salary=120000,
            ),
            Employee(
                name="Jane Smith",
                position="Manager",
                department_id=management_department.id,
                hire_date=None,
                salary=80000,
            ),
            if not User.query.first():
                test = User(username="test")
                test.set_password("test")
                db.session.add(test)
                db.session.commit()
                print("🎉 Created test username: test / password: test")
        ]

        # Use normal ORM to persist relationships correctly
        db.session.add_all(sample_employees)
        db.session.commit()