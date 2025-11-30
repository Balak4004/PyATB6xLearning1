

import requests

try:
    url = input("enter the URL\t")
#response = requests.get("https://google.com")
#response = requests.get("https://api.example.com/data.com")
    response = requests.get(url, timeout=10)
    print(response.status_code)
except requests.exceptions.ConnectionError:
    print("Error due to wrong URL or Connection failed")
except requests.exceptions.Timeout:
    print("Error due to page not opened within given time")
except Exception as e:
    print(e)