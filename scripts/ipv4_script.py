import requests


def get_public_ip():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("ip", "IP not found")
    except Exception as e:
        return f"Error: {e}"
