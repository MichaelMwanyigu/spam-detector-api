from fastapi.testclient import TestClient
from src.api.main import app
import pytest

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json = {"message": "free money now"})
    assert response.status_code == 200
    assert response.json()["message"] in ["ham", "spam"]