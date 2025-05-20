import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get(endpoint):
        return requests.get(f"{APIClient.BASE_URL}/{endpoint}")

    @staticmethod
    def post(endpoint, data):
        return requests.post(f"{APIClient.BASE_URL}/{endpoint}", json=data)

    @staticmethod
    def put(endpoint, data):
        return requests.put(f"{APIClient.BASE_URL}/{endpoint}", json=data)

    @staticmethod
    def delete(endpoint):
        return requests.delete(f"{APIClient.BASE_URL}/{endpoint}")

