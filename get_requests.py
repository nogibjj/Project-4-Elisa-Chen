import requests

def get_activity():
    url = "https://www.boredapi.com/api/activity"
    Data = requests.get(url)
    json_data = Data.json()
    return json_data