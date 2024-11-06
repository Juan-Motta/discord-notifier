import requests  # type: ignore
import os

# Environment variables
WEB_SERVER_URL = os.getenv("WEB_SERVER_URL")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TIME = os.getenv("TIME", 60)
NOTIFY_AT_NIGHT = os.getenv("NOTIFY_AT_NIGHT", "false")

def query_web_server():
    try:
        print(WEB_SERVER_URL)
        response = requests.get(WEB_SERVER_URL)
        print(f"""Status code: {response.status_code} at {time.strftime("%H:%M")}""")
        if int(response.status_code) != 200:
            send_failure_to_discord(f"Error querying web server. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error querying web server {e}")
        send_failure_to_discord(str(e))


def send_failure_to_discord(message):
    print("Validating if we should notify")
    notify = True
    # Notify only during the day
    if NOTIFY_AT_NIGHT == "false":
        hour = int(time.strftime("%H"))
        if  hour > 2 and hour < 13:
            print("Not notifying at night")
            notify = False
    if notify:
        print(f"Sending message to discord: {message}")
        requests.post(
            DISCORD_WEBHOOK_URL,
            json={"username": "Error backend", "content": message},
        )


if __name__ == "__main__":
    import time

    while True:
        print("Querying web server...")
        query_web_server()
        time.sleep(int(TIME))
