import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
sys.path.append(grandparent_dir)

from datetime import datetime
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.model.user import user_info
from app.view import router

app = FastAPI()
app.include_router(router, prefix="/v1")
client = TestClient(app)


@pytest.fixture
def mock_user_info():
    user_info.get_user = Mock(
        return_value={"user_id": "123", "score": 10, "last_login": datetime.now()}
    )
    user_info.update_user = Mock()


def test_add_score_endpoint(mock_user_info):
    request_data = {"user_id": 5, "role": "staff", "score": 5}

    response = client.post("v1/role/score:calculate", json=request_data)

    assert response.status_code == 200
    response_data = response.json()

    # Check if the user's score has been updated correctly
    assert response_data["score"] == 15
