import requests
import json
import argparse

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
    parser = argparse.ArgumentParser(description="Send GitHub dispatch event")
    parser.add_argument("repo", help="Repository name")
    parser.add_argument("pat", help="Personal access token (PAT)")
    parser.add_argument("event_type", help="Event type")
    parser.add_argument("emitter_image", help="Emitter image")

    args = parser.parse_args()

    success = send_github_dispatch(args.repo, args.pat, args.event_type, args.emitter_image)
    if success:
        print("GitHub dispatch event sent successfully.")
    else:
        print("Failed to send GitHub dispatch event.")