import httpx

login_payload = {
    "email" : "test@test.com",
    "password": "test"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data["token"]["accessToken"]
user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {access_token}"})
print(user_response.json())
print(f"Status code: {user_response.status_code}")