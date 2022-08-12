from main import app
from fastapi.testclient import TestClient


def test_read_main():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {
            "message": "Wikipedia Here we go!!!. Call /search or /wiki endpoints"
        }


def test_read_search():
    with TestClient(app) as client:
        response = client.get("/search/Barack Obama")
        assert response.status_code == 200
        assert "Barack" in response.text