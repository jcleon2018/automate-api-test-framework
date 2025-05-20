import os
import sys
import pytest
import jsonschema


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from api_test.utils.api_client import APIClient
from api_test.config.schemas import comment_schema
from api_test.utils.data_loader import DataLoader
from api_test.utils.logger import logger

test_data = DataLoader.load_data()

def test_create_comment():
    """Test Create (POST)"""
    response = APIClient.post("posts/1/comments", test_data["valid_comment"])
    logger.debug(f"Create Comment Response: {response.json()}")

    assert response.status_code == 201
    assert response.json()["name"] == test_data["valid_comment"]["name"]
    jsonschema.validate(instance=response.json(), schema=comment_schema)

def test_get_comment():
    """Test Read (GET)"""
    response = APIClient.get("posts/1/comments")
    logger.debug(f"Get Comments Response: {response.json()}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "name" in response.json()[0]
    jsonschema.validate(instance=response.json()[0], schema=comment_schema)

@pytest.mark.skip(reason="Placeholder does not support updating comments")
def test_update_comment():
    pass


@pytest.mark.skip(reason="Placeholder does not support deleting comments")
def test_delete_comment():
    pass

