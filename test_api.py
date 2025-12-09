"""
API Test Script
This script demonstrates how to interact with the Auth App API
"""

import requests
import json

# Base URL - change this if testing on different device
BASE_URL = "http://localhost:5000"

def test_register():
    """Test user registration"""
    print("\n--- Testing Registration ---")
    
    url = f"{BASE_URL}/api/register"
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }
    
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    return response.status_code == 201

def test_login():
    """Test user login"""
    print("\n--- Testing Login ---")
    
    url = f"{BASE_URL}/api/login"
    data = {
        "username": "testuser",
        "password": "password123"
    }
    
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    return response.status_code == 200

def test_get_users():
    """Test getting all users (requires authentication)"""
    print("\n--- Testing Get Users ---")
    
    # First login to create a session
    session = requests.Session()
    login_url = f"{BASE_URL}/api/login"
    login_data = {
        "username": "testuser",
        "password": "password123"
    }
    session.post(login_url, json=login_data)
    
    # Now get users
    users_url = f"{BASE_URL}/api/users"
    response = session.get(users_url)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_duplicate_register():
    """Test that duplicate registration fails"""
    print("\n--- Testing Duplicate Registration ---")
    
    url = f"{BASE_URL}/api/register"
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }
    
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("✓ Correctly rejected duplicate registration!" if response.status_code == 400 else "✗ Should have rejected!")

def test_wrong_password():
    """Test that wrong password fails"""
    print("\n--- Testing Wrong Password ---")
    
    url = f"{BASE_URL}/api/login"
    data = {
        "username": "testuser",
        "password": "wrongpassword"
    }
    
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("✓ Correctly rejected wrong password!" if response.status_code == 401 else "✗ Should have rejected!")

def main():
    """Run all tests"""
    print("=" * 50)
    print("Auth App API Test Suite")
    print("=" * 50)
    print(f"\nTesting against: {BASE_URL}")
    print("\nMake sure the Flask app is running!")
    print("Run: python app.py")
    print("-" * 50)
    
    try:
        # Test registration (first time)
        if test_register():
            print("\n✓ Registration successful!")
        
        # Test login
        if test_login():
            print("\n✓ Login successful!")
        
        # Test getting users
        test_get_users()
        
        # Test error cases
        test_duplicate_register()
        test_wrong_password()
        
        print("\n" + "=" * 50)
        print("All tests completed!")
        print("=" * 50)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the server!")
        print("Make sure the Flask app is running on http://localhost:5000")
        print("Run: python app.py")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
