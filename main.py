import requests

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": "ryC7YTsmnDf7Bc57",
    "username": "nas13",
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=parameters)
print(response.text)