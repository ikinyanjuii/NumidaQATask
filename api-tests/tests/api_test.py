import requests

BASE_URL = "http://localhost:5001"

def get_authenticated_session():
    session = requests.Session()
    # Request OTP
    otp_request_payload = {
        "phone_number": "0712345678"
    }
    response = session.post(
        f"{BASE_URL}/api/auth/request-otp",
        json=otp_request_payload
    )
    assert response.status_code == 200
    # Verify OTP
    otp_verify_payload = {
        "phone_number": "0712345678",
        "otp": "0000"
    }
    response = session.post(
        f"{BASE_URL}/api/auth/verify-otp",
        json=otp_verify_payload
    )
    assert response.status_code == 200
    return session

# ------------------
# Test Cases
# ------------------
#Request OTP
def test_request_otp():
    payload = {"phone_number": "0712345678"}
    response = requests.post(f"{BASE_URL}/api/auth/request-otp", json=payload)
    assert response.status_code == 200
#Verify OTP
def test_verify_otp():
    session = requests.Session()

    session.post(
        f"{BASE_URL}/api/auth/request-otp",
        json={"phone_number": "0712345678"}
    )

    response = session.post(
        f"{BASE_URL}/api/auth/verify-otp",
        json={"phone_number": "0712345678", "otp": "0000"}
    )
    assert response.status_code == 200
#Get Loans - Unauthenticated
def test_get_loans_unauthenticated():
    response = requests.get(f"{BASE_URL}/api/application/status")
    assert response.status_code == 401
#API Health Check
def test_health_check():
    response = requests.get(f"{BASE_URL}/api/health")
    assert response.status_code == 200