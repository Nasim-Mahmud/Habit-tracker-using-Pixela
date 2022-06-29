import requests


USER_NAME = "nas13"
TOKEN = "ryC7YTsmnDf7Bc57"
pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=parameters)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_parameters= {
    "id":,
    "name":,
    "unit":,
    "type":,
    "color":,
}
requests.post()