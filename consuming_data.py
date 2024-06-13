import requests
import json

# Your API endpoint and access token
query_endpoint = "https://api.workflow.prod.trulioo.com/v2/query/client/{clientId}"
access_token = "your_access_token_here"
query_client_id = "client_id_to_query"

# Function to query workflow data using the access token
def query_workflow_data(access_token, client_id):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(query_endpoint.format(clientId=client_id), headers=headers)
    if response.status_code == 200:
        print("Workflow data retrieved successfully.")
        print("Response:", json.dumps(response.json(), indent=2))
    else:
        print(f"Failed to retrieve workflow data. Status code: {response.status_code}")
        print("Error response:", response.json())

# Execute the function to query workflow data
query_workflow_data(access_token, query_client_id)





# Replace your_access_token_here: Insert your actual access token.
# Replace client_id_to_query: Insert the actual client ID you want to query.
# Query Workflow Data: The query_workflow_data function retrieves workflow data for the specified client using the provided access token.
# Run the Script: Execute the script to query the workflow data.