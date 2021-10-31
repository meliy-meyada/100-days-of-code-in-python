import requests
from datetime import datetime

USERNAME = "YOUR Username"
TOKEN = "Your TOKEN"
GRAPH_ID = "Your Graph ID"

pixela_endpoint = "https://pixe.la/v1/users"



user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}



response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Kilometers did you cycle today? "),

}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_pixel_data = {
    "quantity": "4.5"
}

response = requests.put(url=update_endpoint, json=update_pixel_data, headers=headers)
print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)