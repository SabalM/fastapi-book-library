from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Book Library API!"}


def test_search_endpoint():
    response = client.get("/search?title=python")
    assert response.status_code == 200
    data = response.json()
    assert "docs" in data


def test_ui_page():
    response = client.get("/ui")
    assert response.status_code == 200
    assert "Search Books" in response.text  # Confirms HTML page renders
