import requests

# Your API endpoint and client credentials
token_endpoint = "https://auth-api.trulioo.com/connect/token"
client_id = "your_client_id_here"
client_secret = "your_client_secret_here"

# Data for the token request
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials',
    'scope': 'workflow.studio.api'
}

# Headers for the request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Make the POST request to get the access token
response = requests.post(token_endpoint, headers=headers, data=payload)

# Check the response
if response.status_code == 200:
    access_token_data = response.json()
    access_token = access_token_data["access_token"]
    print("Access token retrieved successfully.")
    print("Access Token:", access_token)
else:
    print(f"Failed to retrieve access token. Status code: {response.status_code}")
    print("Error response:", response.json())






# Replace your_client_id_here and your_client_secret_here: Insert your actual client ID and client secret.
# Make the Request: Run the script to make a POST request to the OAuth token endpoint and retrieve the access token.
# Check the Response: The script will print the access token if the request is successful.
