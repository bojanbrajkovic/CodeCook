import requests
import json
import hmac
import hashlib

# Your API endpoint and key
api_endpoint = "https://your.callback.url"
api_key = "your_api_key_here"
secret = "your_secret_here"

# Simulated received data (normally you'd get this from the received event)
received_data = {
    "token": "your_verification_token",
    "challenge": "challenge_value_here",
    "type": "url_verification"
}
received_payload = json.dumps(received_data)

# Calculate HMAC for the received payload
signature = hmac.new(secret.encode(), received_payload.encode(), hashlib.sha256).hexdigest()

# Simulated headers of received request
headers = {
    "x-trulioo-signature": signature
}

# Function to handle verification request
def handle_verification_request(data, headers):
    # Verify the HMAC signature
    calculated_hmac = hmac.new(secret.encode(), json.dumps(data).encode(), hashlib.sha256).hexdigest()
    if headers.get("x-trulioo-signature") != calculated_hmac:
        return "Invalid signature", 403
    
    # Respond with the challenge attribute value
    response = {
        "challenge": data["challenge"]
    }
    return response, 200




# Replace your_api_key_here and your_secret_here: Insert your actual API key and secret.
# Simulated Data: In a real scenario, the received_data and headers would come from the actual HTTP POST request sent to your endpoint.
# Calculate HMAC: This step ensures the received payload is authentic.
# Respond to Challenge: The handle_verification_request function checks the HMAC signature and returns the required challenge response.
# Integration with a Web Framework: For actual deployment, integrate this logic into a web server using a framework like Flask