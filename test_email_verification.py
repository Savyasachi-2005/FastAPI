#!/usr/bin/env python3
"""
Test script to debug email verification
Run this script to test the email verification process step by step
"""

import requests
import json
from JWTtoken import create_email_token, verify_email_token

# Configuration
BASE_URL = "http://localhost:8000"
TEST_EMAIL = "test@example.com"

def test_token_creation():
    """Test JWT token creation and verification"""
    print("🔧 Testing JWT token creation and verification...")
    
    # Create token
    token = create_email_token(TEST_EMAIL)
    print(f"✅ Token created: {token[:20]}...")
    
    # Verify token
    try:
        email = verify_email_token(token)
        print(f"✅ Token verified, email: {email}")
        return token
    except Exception as e:
        print(f"❌ Token verification failed: {e}")
        return None

def test_email_verification_endpoint(token):
    """Test the email verification endpoint"""
    print(f"\n🔧 Testing email verification endpoint...")
    
    url = f"{BASE_URL}/verify-email?token={token}"
    print(f"📡 Requesting: {url}")
    
    try:
        response = requests.get(url)
        print(f"📊 Status Code: {response.status_code}")
        print(f"📄 Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ Email verification endpoint working!")
        else:
            print("❌ Email verification endpoint failed!")
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure FastAPI is running on localhost:8000")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_celery_task():
    """Test Celery task directly"""
    print(f"\n🔧 Testing Celery task...")
    
    try:
        from celery_worker import send_email_task
        
        # Test the task directly (without delay)
        result = send_email_task(TEST_EMAIL, "test_token_123")
        print(f"✅ Celery task result: {result}")
        
    except Exception as e:
        print(f"❌ Celery task failed: {e}")

def main():
    print("🚀 Email Verification Debug Test")
    print("=" * 50)
    
    # Test 1: JWT Token
    token = test_token_creation()
    
    if token:
        # Test 2: Email verification endpoint
        test_email_verification_endpoint(token)
        
        # Test 3: Celery task
        test_celery_task()
    
    print("\n" + "=" * 50)
    print("🏁 Debug test completed!")

if __name__ == "__main__":
    main() 