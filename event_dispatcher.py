

import hmac
import hashlib
import json
import sys

# Secret key for HMAC verification
SECRET_KEY = 'your_secret_key'

# List of event types
EVENT_TYPES = [
    "FLOW_START", "STEP_INIT", "STEP_SUBMIT", "SERVICE_INIT",
    "INTERMEDIATE_EVENT_RECEIVED", "SERVICE_SUBMIT", "SERVICE_TIMEOUT",
    "FLOW_END", "MANUALLY_ACCEPTED", "MANUALLY_REJECTED",
    "MANUALLY_PENDING_REVIEW", "NOTE_ADDED", "TASK_ADDED",
    "TASK_DONE", "TASK_UNDONE", "URL_VERIFICATION"
]

# List of service types
SERVICE_TYPES = [
    "TWILIO", "TRULIOO_EIDV", "TRULIOO_KYB_SEARCH", "TRULIOO_KYB_VERIFY",
    "TRULIOO_KYB_INSIGHTS", "TRULIOO_KYB_COMPLETE", "TRULIOO_DOCV",
    "TRULIOO_UTILITY_ID", "TRULIOO_PERSON_WL", "TRULIOO_BUSINESS_WL",
    "TRULIOO_ELECTRONIC_ID", "TRULIOO_KYB_SUBMITTER", "SHARED_SIGNING",
    "ACCEPT", "REJECT"
]

def verify_signature(payload, signature):
    """Verify the HMAC signature."""
    digest = hmac.new(SECRET_KEY.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(digest, signature)

def process_event(event_type, service_type, event):
    """Process the incoming event based on event type and service type."""
    if event_type == 'FLOW_START':
        handle_flow_start(event)
    elif event_type == 'STEP_INIT':
        handle_step_init(event)
    elif event_type == 'SERVICE_SUBMIT' and service_type in SERVICE_TYPES:
        handle_service_submit(service_type, event)
    else:
        sys.stdout.write(f"Unhandled event type or service type: {event_type}, {service_type}\n")

def handle_flow_start(event):
    """Handle the FLOW_START event."""
    sys.stdout.write(f"Flow started: {json.dumps(event)}\n")

def handle_step_init(event):
    """Handle the STEP_INIT event."""
    sys.stdout.write(f"Step initiated: {json.dumps(event)}\n")

def handle_service_submit(service_type, event):
    """Handle the SERVICE_SUBMIT event based on service type."""
    if service_type == 'TWILIO':
        handle_twilio_service(event)
    elif service_type == 'TRULIOO_EIDV':
        handle_trulioo_eidv_service(event)
    else:
        sys.stdout.write(f"Unhandled service type: {service_type}\n")

def handle_twilio_service(event):
    """Handle Twilio service events."""
    sys.stdout.write(f"Twilio service event: {json.dumps(event)}\n")

def handle_trulioo_eidv_service(event):
    """Handle Trulioo EIDV service events."""
    sys.stdout.write(f"Trulioo EIDV service event: {json.dumps(event)}\n")

# Add more handler functions for other service types as needed

def main():
    # Example JSON payload and signature (for demonstration)
    example_payload = '{"event": {"type": "SERVICE_SUBMIT"}, "serviceType": "TWILIO", "data": "example"}'
    example_signature = hmac.new(SECRET_KEY.encode(), example_payload.encode(), hashlib.sha256).hexdigest()

    # Simulate reading JSON payload from a file or incoming request
    event = json.loads(example_payload)
    signature = example_signature

    # Verify signature
    if verify_signature(example_payload, signature):
        event_type = event.get('event', {}).get('type')
        service_type = event.get('serviceType')
        if event_type in EVENT_TYPES:
            process_event(event_type, service_type, event)
        else:
            sys.stdout.write("Event type not supported\n")
    else:
        sys.stdout.write("Invalid signature\n")

if __name__ == '__main__':
    main()
