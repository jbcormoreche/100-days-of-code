# API Post Requests and Headers

# HTTP Requests
# A GET request is used to ask an external system for a particular piece of data and to get it in the response.
# A POST request is used to give an external system some piece of data.
# A PUT request is used to update a piece of data in an external system.
# A DELETE request is used to delete a piece of data in an external system.

# API Headers allow data not to be passed in the request itself but instead in the header.

# Day 37 Project - Habit Tracking
import requests
from datetime import datetime

USERNAME = "angela"
TOKEN = "hjkh34h3jk4hj34h3jh4"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/vl/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create an account
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

# Identification with headers
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Post data
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Format the date
today = datetime.now()
# today = datetime(year=2020, month=7, day=23)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Update data
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5",
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# Delete data
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
