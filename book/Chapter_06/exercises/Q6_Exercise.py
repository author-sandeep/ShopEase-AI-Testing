import requests
def execute_strict_timeout():
    return requests.post("https://api.shopease.com", json={"test": 1}, timeout=3.5)