import pytest
from backend.app.app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello_endpoint(client):
    rv = client.get("/api/hello")
    assert rv.status_code == 200
    j = rv.get_json()
    assert j["message"] == "Hello from Flask!"