import requests
import json
import jsonpath

def test_oauth_api():
    token_url = "http://thetestingworldapi.com/Token"
    data = {"grant_type": "password", "username": "admin", "password": ""}
    response = requests.post(token_url, data)
    print(response.text)
    token_value = jsonpath.jsonpath(response.json, "access_token")

    auth = {"Authorization": "Bearer " + token_value[0]}
    API_URL = "http://thetestingworldapi.com/api/StDetails/1104"
    response = requests.get(API_URL, header=auth)
    print(response.text)

