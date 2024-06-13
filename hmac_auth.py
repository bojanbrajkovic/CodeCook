import hmac
import hashlib
import json

# Your secret key
secret = "your_secret_here"

# Simulated received payload and signature (in practice, these would come from the actual request)
received_payload = {
    "token": "your_verification_token",
    "challenge": "challenge_value_here",
    "type": "url_verification"
}
received_payload_str = json.dumps(received_payload)
received_signature = "received_hmac_signature_here"

# Function to verify HMAC signature
def verify_hmac_signature(payload, received_signature, secret):
    # Calculate HMAC for the received payload
    calculated_hmac = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    # Compare the calculated HMAC with the received signature
    return hmac.compare_digest(calculated_hmac, received_signature)

# Verify the received signature
is_valid_signature = verify_hmac_signature(received_payload_str, received_signature, secret)

if is_valid_signature:
    print("The HMAC signature is valid.")
else:
    print("The HMAC signature is invalid.")

# Example function to handle verification request
def handle_verification_request(data, headers):
    received_signature = headers.get("x-trulioo-signature")
    payload_str = json.dumps(data)
    
    if verify_hmac_signature(payload_str, received_signature, secret):
        response = {"challenge": data["challenge"]}
        return response, 200
    else:
        return "Invalid signature", 403

# Simulate handling the request
headers = {
    "x-trulioo-signature": received_signature
}
response, status_code = handle_verification_request(received_payload, headers)
print(f"Response: {response}, Status Code: {status_code}")






# Replace your_secret_here: Insert your actual secret key.
# Simulated Data: In a real scenario, received_payload and headers would come from the actual HTTP POST request.
# Verify HMAC Signature: The verify_hmac_signature function calculates the HMAC of the received payload and compares it with the signature in the x-trulioo-signature header.
# Handle Verification Request: The handle_verification_request function checks the HMAC signature and returns the required challenge response.