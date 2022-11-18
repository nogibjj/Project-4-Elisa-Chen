import requests

def get_activity(activity_type = ''):
    if activity_type == '':
        url = "https://www.boredapi.com/api/activity/"
    else:
        url = "http://www.boredapi.com/api/activity?type=" + activity_type
    Data = requests.get(url, timeout = 20)
    json_data = Data.json()
    print(json_data)
    return json_data

if __name__ == "__main__":
    get_activity()