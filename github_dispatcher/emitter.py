import requests
import json
import sys

def send_github_dispatch(repo, pat, event_type, emitter_image):
    url = f"https://api.github.com/repos/{repo}/dispatches"
    headers = {
        "Accept": "application/vnd.github.everest-preview+json",
        "Authorization": f"Bearer {pat}"
    }
    data = {
        "event_type": event_type,
        "client_payload": {
            "emitter_image": emitter_image
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 204:
        print("GitHub dispatch event sent successfully. Status code:", response.status_code)
        return True
    else:
        print("Failed to send GitHub dispatch event. Status code:", response.status_code)
        return False
    
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python github_dispatcher.py <repo> <pat> <event_type> <emitter_image>")
    else:
        repo = sys.argv[1]
        pat = sys.argv[2]
        event_type = sys.argv[3]
        emitter_image = sys.argv[4]
        success = send_github_dispatch(repo, pat, event_type, emitter_image)
        if success:
            print("GitHub dispatch event sent successfully.")
        else:
            print("Failed to send GitHub dispatch event.")