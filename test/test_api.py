from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query():

    response = client.post(
        "/query",
        json={"question":"total students"}
    )

    assert response.status_code == 200


def test_stats():

    response = client.get("/stats")

    assert response.status_code == 200