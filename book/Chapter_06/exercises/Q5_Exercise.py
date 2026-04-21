import os

secure_headers = {
    "Authorization": f"Bearer {os.getenv('API_KEY')}",
    "Content-Type": "application/json"
}