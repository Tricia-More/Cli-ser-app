import requests
count = 5
for i in range(10):
    lin = str(input("Client: "))
    url = "http://127.0.0.1:8000/api/"+(lin)+"/"
    response = requests.get(url)
    

    if response.status_code == 200:
        print("Request Sent to:", response.url)
        print( response.json())
    else:
        print("Failed to Connect to Server")
    