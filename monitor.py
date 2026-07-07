import requests
import time
from datetime import datetime
import json
import os
from dotenv import load_dotenv


load_dotenv() 


WEBHOOK_URL = os.environ.get("ALERT_WEBHOOK")

# A list of URLs to monitor. 
# We include httpstat.us to intentionally simulate a 500 Internal Server Error for testing.
URLS_TO_CHECK = [
    "https://www.google.com",
    "https://www.github.com",
    "https://httpstat.us/500" 
]

def send_alert(url, status_code, error_message="None"):
    """Formats and sends an incident alert to the webhook."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Formatting a professional alert payload
    payload = {
        "username": " SRE Incident Bot",
        "embeds": [
            {
                "title": "🚨 SEV-1 INCIDENT DETECTED 🚨",
                "description": f"An endpoint has failed health checks and requires immediate attention.",
                "color": 16711680, # Red color for critical alerts
                "fields": [
                    {"name": "Affected Endpoint", "value": url, "inline": False},
                    {"name": "Status Code", "value": str(status_code), "inline": True},
                    {"name": "Time of Failure", "value": timestamp, "inline": True},
                    {"name": "Error Details", "value": error_message, "inline": False},
                    {"name": "Action Required", "value": "**SLA: 30 minutes to acknowledge.** Assign an engineer immediately.", "inline": False}
                ]
            }
        ]
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 204:
        print(f"[{timestamp}] Alert successfully escalated for {url}")
    else:
        print(f"[{timestamp}] Failed to send alert.")

def check_urls():
    """Loops through URLs and checks their health."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Running health checks...")
    
    for url in URLS_TO_CHECK:
        try:
            # Send a GET request with a 5-second timeout
            response = requests.get(url, timeout=5)
            
            # If the status code is 400 or higher, it's an error
            if response.status_code >= 400:
                send_alert(url, response.status_code, response.reason)
            else:
                print(f" - {url} is ONLINE (Status {response.status_code})")
                
        except requests.exceptions.RequestException as e:
            # Catches timeouts, DNS failures, or connection refusals
            send_alert(url, "OFFLINE", str(e))


if __name__ == "__main__":
    print("Starting SRE Monitoring Service...")
    while True:
        check_urls()
        # Wait 60 seconds before checking again to avoid spamming networks
        time.sleep(60)