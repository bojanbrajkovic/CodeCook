import requests
import json

# API endpoint and your API key
api_endpoint = "https://api.workflow.prod.trulioo.com/interpreter-v2/end-clients"
api_key = "your_api_key_here"

# Data for the request
payload = {
    "from": "end_client_id_from",
    "to": "end_client_id_to",
    "type": "RELATES_TO"  # Link type: "RELATES_TO", "DUPLICATE_OF", "OWNS", "OWNED_BY"
}

# Headers for the request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Make the POST request
response = requests.post(api_endpoint, headers=headers, data=json.dumps(payload))

# Check the response
if response.status_code == 201:
    print("Link created successfully.")
    print("Response:", response.json())
else:
    print(f"Failed to create link. Status code: {response.status_code}")
    print("Error response:", response.json())







# Put in your API key: Change your_api_key_here to your actual API key.
# Add End Client IDs: Replace end_client_id_from and end_client_id_to with the IDs of the clients you want to link.
# Set Link Type: Choose the link type that fits your needs: "RELATES_TO", "DUPLICATE_OF", "OWNS", or "OWNED_BY".
# Run it: Run the script. If it works, you'll see a success message and the response. If not, you'll get an error message with details.