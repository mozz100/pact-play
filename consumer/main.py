import os

import requests


def user(user_name):
    """Fetch a user object by user_name from the server."""
    SERVER_PORT = int(os.environ.get("SERVER_PORT", "80"))
    SERVER_HOST = os.environ.get("SERVER_HOST", "www.example.com")
    SERVER_URL = os.environ.get("SERVER_URL", f"http://{SERVER_HOST}:{SERVER_PORT}")

    uri = f"{SERVER_URL}/users/{user_name}.json"

    return requests.get(uri).json()
