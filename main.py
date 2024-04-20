import requests  # type: ignore
import os

# Environment variables
WEB_SERVER_URL = os.getenv("WEB_SERVER_URL")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TIME = os.getenv("TIME", 60)


def query_web_server():
    try:
        response = requests.get(WEB_SERVER_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        send_failure_to_discord(str(e))


def send_failure_to_discord(message):
    requests.post(
        DISCORD_WEBHOOK_URL,
        json={"username": "test", "content": "hello"},
    )


if __name__ == "__main__":
    import time

    while True:
        print("Querying web server...")
        query_web_server()
        time.sleep(int(TIME))
