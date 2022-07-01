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

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

#Generating graph in Pixela
# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
#
# graph_parameters = {
#     "id": "graph01",
#     "name": "Studying Graph",
#     "unit": "Hour",
#     "type": "float",
#     "color": "shibafu",
# }
#
# secure_headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=secure_headers)
# print(response.text)

# Generating a pixel
pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph01"

pixel_parameters = {
    "date": "20220701",
    "quantity": "10",

}
secure_headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.get(url=pixel_endpoint, json=pixel_parameters, headers=secure_headers)
print(response.text)