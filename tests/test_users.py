from app import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_create_user(mock_db_session):
    data = {"email": "test@gmail.com", "hashed_pass": "string"}
    response = client.post("/users/", data=data)

    assert response.status_code == 200
    data = response.json()

    assert data["email"] == "test@gmail.com"

    mock_db_session.add.assert_called()
    mock_db_session.commit.assert_called()
