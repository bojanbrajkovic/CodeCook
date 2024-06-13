import requests
import json

# API endpoint and your API key
initialize_endpoint = "https://api.workflow.prod.trulioo.com/interpreter-v2/flow/{flowId}"
submit_endpoint = "https://api.workflow.prod.trulioo.com/interpreter-v2/submit/{flowId}"
api_key = "your_api_key_here"
flow_id = "your_flow_id_here"

# Headers for the request
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Make the GET request to initialize the flow
response = requests.get(initialize_endpoint.format(flowId=flow_id), headers=headers)

# Check the response
if response.status_code == 200:
    print("Flow initialized successfully.")
    print("Response:", response.json())
else:
    print(f"Failed to initialize flow. Status code: {response.status_code}")
    print("Error response:", response.json())
    exit()

# Extract session ID from the response headers
session_id = response.headers.get('x-hf-session')
if not session_id:
    print("Session ID not found in the response headers. Cannot proceed.")
    exit()

# Data to be submitted for the current step
payload = {
    # Add the required data fields as per your flow's requirements
    "field1": "value1",
    "field2": "value2"
}

# Update headers for the submit request
headers.update({
    "Content-Type": "application/json",
    "x-hf-session": session_id
})

# Make the POST request to submit the data
response = requests.post(submit_endpoint.format(flowId=flow_id), headers=headers, data=json.dumps(payload))

# Check the response
if response.status_code == 200:
    print("Data submitted successfully.")
    print("Response:", response.json())
else:
    print(f"Failed to submit data. Status code: {response.status_code}")
    print("Error response:", response.json())




# Put in your API key: Change your_api_key_here to your actual API key.
# Add Flow ID: Replace your_flow_id_here with the actual ID of your flow.
# Add Data Fields: Update the payload with the data fields required for your current step.
# Run the Script: Execute the script. It will initialize the flow, extract the session ID from the response headers, and submit the data for the current step.