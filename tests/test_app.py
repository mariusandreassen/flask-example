import pytest
from app import app, db, Employee
from datetime import date 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # use in-memory DB
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_index_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Employees" in response.data

def test_add_employee(client):
    response = client.post('/add', data={
        'name': 'Test User',
        'position': 'Tester',
        'department': 'QA',
        'hire_date': '2024-1-1',
        'salary': 50000
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Test User" in response.data