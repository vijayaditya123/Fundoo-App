from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/",
        json={
            "full_name": "Test User",
            "email": "testuser@gmail.com",
            "password": "12345"
        }
    )
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@gmail.com"


def test_get_all_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_by_id():
    response = client.post(
        "/users/",
        json={
            "full_name": "Second User",
            "email": "seconduser@gmail.com",
            "password": "12345"
        }
    )
    user_id = response.json()["user_id"]

    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json()["user_id"] == user_id


def test_update_user():
    response = client.post(
        "/users/",
        json={
            "full_name": "Update User",
            "email": "updateuser@gmail.com",
            "password": "12345"
        }
    )
    user_id = response.json()["user_id"]

    update_response = client.put(
        f"/users/{user_id}",
        json={
            "full_name": "Updated Name",
            "email": "updated@gmail.com",
            "password": "67890"
        }
    )
    assert update_response.status_code == 200
    assert update_response.json()["full_name"] == "Updated Name"


def test_delete_user():
    response = client.post(
        "/users/",
        json={
            "full_name": "Delete User",
            "email": "deleteuser@gmail.com",
            "password": "12345"
        }
    )
    user_id = response.json()["user_id"]

    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200

