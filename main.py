from datetime import datetime
import requests

USER_NAME = "nas13"
TOKEN = "ryC7YTsmnDf7Bc57"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph01"

parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

# Generating graph in Pixela
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Studying Graph",
    "unit": "Hour",
    "type": "float",
    "color": "shibafu",
}

secure_headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=secure_headers)
# print(response.text)

# Generating a pixel
pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

pixel_parameters = {
    "date": today_formatted,
    "quantity": input("How many hours you studied todays?\n"),

}
response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=secure_headers)
print(response.text)

## Updating and deleting a pixel.
# Updating
pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today_formatted}"

pixel_update_parameter = {
    "quantity": "2.5",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_parameter, headers=secure_headers)
# print(response.text)

# Deleting
pixel_delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today_formatted}"

# response = requests.delete(url=pixel_delete_endpoint, headers=secure_headers)
# print(response.text)
