import requests
 
url = "http://127.0.0.1:8000/api/hello/"
response = requests.get(url)

if response.status_code == 200:
    print("Server Response:", response.json())
else:
    print("Failed to Connect to Server")