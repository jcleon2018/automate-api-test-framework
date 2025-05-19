import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from api_test.utils.api_client import APIClient
from api_test.utils.logger import logger
from api_test.utils.data_loader import DataLoader


test_data = DataLoader.load_data()

def test_create_post():
    response = APIClient.post("posts", test_data["valid_post"])
  
    logger.debug(f"Response Status: {response.status_code}")
    logger.debug(f"Response JSON: {response.json()}")
    assert response.status_code == 201
    assert response.json()["title"] == test_data["valid_post"]["title"]

def test_get_post():
    response = APIClient.get("posts/1")
    
    logger.debug(f"Response Status: {response.status_code}")
    logger.debug(f"Response JSON: {response.json()}")
    assert response.status_code == 200
    assert "title" in response.json()

def test_update_post():
    response = APIClient.put("posts/1", test_data["updated_post"])
    
    logger.debug(f"Response Status: {response.status_code}")
    logger.debug(f"Response JSON: {response.json()}")
    assert response.status_code == 200
    assert response.json()["title"] == "updated"

def test_delete_post():
    response = APIClient.delete("posts/1")

    logger.debug(f"Response Status: {response.status_code}")
    logger.debug(f"Response JSON: {response.json()}")
    assert response.status_code == 200
