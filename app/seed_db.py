def seed_database(db, Employee):
    """Seed the database with initial sample data if empty."""
    if Employee.query.first():
        print("Database already seeded.")
        return

    sample_employees = [
        Employee(name="Hennig Olsen", position="CEO", department="Management", hire_date=None, salary=120000),
        Employee(name="Rasmus Olsen", position="Developer", department="Tech", hire_date=None, salary=85000),
    ]

    db.session.bulk_save_objects(sample_employees)
    db.session.commit()
    print("Database seeded with initial data.")