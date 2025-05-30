import pytest
from main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}

def test_add(client):
    response = client.get('/add/2/3')
    assert response.status_code == 200
    assert response.get_json() == {"result": 5}
