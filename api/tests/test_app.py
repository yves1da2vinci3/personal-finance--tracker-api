import requests

def test_register():
    """Tests the register endpoint."""
    data = {"username": "test_user", "password": "password"}
    response = requests.post("http://localhost:5000/auth/register", json=data)
    assert response.status_code == 201
    assert response.json()["message"] == "User registered"

def test_login():
    """Tests the login endpoint."""
    data = {"username": "test_user", "password": "password"}
    response = requests.post("http://localhost:5000/auth/login", json=data)
    assert response.status_code == 200
    assert response.json()["token"]

def test_get_incomes():
    """Tests the get incomes endpoint."""
    response = requests.get("http://localhost:5000/incomes")
    assert response.status_code == 200
    assert response.json() == []

def test_create_income():
    """Tests the create income endpoint."""
    data = {"name": "Salary", "amount": 1000, "date": "2023-08-14"}
    response = requests.post("http://localhost:5000/incomes", json=data)
    assert response.status_code == 201
    assert response.json()["name"] == "Salary"
    assert response.json()["amount"] == 1000
    assert response.json()["date"] == "2023-08-14"

def test_update_income():
    """Tests the update income endpoint."""
    data = {"id": 1, "name": "Salary", "amount": 2000, "date": "2023-08-15"}
    response = requests.put("http://localhost:5000/incomes", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Salary"
    assert response.json()["amount"] == 2000
    assert response.json()["date"] == "2023-08-15"

def test_delete_income():
    """Tests the delete income endpoint."""
    response = requests.delete("http://localhost:5000/incomes/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Income deleted"

if __name__ == "__main__":
    test_register()
    test_login()
    test_get_incomes()
    test_create_income()
    test_update_income()
    test_delete_income()
