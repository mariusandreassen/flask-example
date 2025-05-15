def seed_database(db, Employee, Department, User):
    """Seed the database with initial sample data if empty."""

    # 1. Create 'test' user if it doesn't exist
    test_user = User.query.filter_by(username="test").first()
    if not test_user:
        test_user = User(username="test")
        test_user.set_password("test")
        db.session.add(test_user)
        db.session.commit()
        print("Created test username: test / password: test")

    # 2. Ensure 'Management' department exists
    management_department = Department.query.filter_by(name="Management").first()
    if not management_department:
        management_department = Department(name="Management")
        db.session.add(management_department)
        db.session.commit()

    # 3. Create 'test Testen' employee linked to test user
    test_employee = Employee.query.filter_by(user_id=test_user.id).first()
    if not test_employee:
        test_employee = Employee(
            name="test Testen",
            position="Test Engineer",
            department_id=management_department.id,
            user_id=test_user.id,
            salary=0,
        )
        db.session.add(test_employee)
        db.session.commit()
        print("Linked 'test' user to employee: test Testen")

    # 4. Seed additional employees if none exist (excluding 'test Testen')
    if Employee.query.count() <= 1:
        other_employees = [
            Employee(
                name="Hennig Olsen",
                position="CEO",
                department_id=management_department.id,
                salary=120000,
            ),
            Employee(
                name="Jane Smith",
                position="Manager",
                department_id=management_department.id,
                salary=80000,
            )
        ]
        db.session.add_all(other_employees)
        db.session.commit()
        print("Seeded additional sample employees.")