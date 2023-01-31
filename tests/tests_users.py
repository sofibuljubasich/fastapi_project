from fastapi.testclient import TestClient
from main import app
import schemas

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.json().get('message') == "Go to the documentation :)"

def test_create_user():
    resp = client.get("/users/",json={"email":"testing@gmail.com","password":"pass123","name":"test"})

    new_user = schemas.UserOut(**resp.json())
    assert new_user.email == "testing@gmail.com"
    assert resp.status_code == 201