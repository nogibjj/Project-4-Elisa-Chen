import requests

def get_activity():
    url = "https://www.boredapi.com/api/activity"
    Data = requests.get(url, timeout = 20)
    json_data = Data.json()
    print(json_data)
    return json_data

if __name__ == "__main__":
    get_activity()