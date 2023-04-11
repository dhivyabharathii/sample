import requests
BASE = "http://127.0.0.1:5004/"
response= requests.put(BASE + "video/1")
print(response.json())