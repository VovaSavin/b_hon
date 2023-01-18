import requests
import json


def get_me(message):
    token = "5671244790:AAEeVlcbFLpfzNJvGIb7gfyskQlludfFvyU"
    response_query = requests.get(
        f"https://api.telegram.org/bot{token}/sendMessage",
        params={"chat_id": 834589499, "text": message}
    )
    return json.loads(response_query.text)
