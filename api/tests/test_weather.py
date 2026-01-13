from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_current_weather():
    response = client.get("/api/weather/current?city=Paris")
    assert response.status_code == 200

    data = response.json()
    assert "city" in data
    assert "country" in data
    assert "weather" in data
    assert "temperature" in data["weather"]
