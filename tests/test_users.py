from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_create_user(mocker):
    mock_db_session = MagicMock()
    mocker.patch("app.db.get_db", return_value=mock_db_session)

    new_user = {"email": "test@gmail.com", "hashed_pass": "123456"}
    response = client.post("/users/", json=new_user)

    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()
