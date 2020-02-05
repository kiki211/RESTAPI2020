import requests
import json
import jsonpath
import pytest

#API URL
url = "https://reqres.in/api/users"
a = 10

@pytest.fixture
def start_exec():
    global file
    file = open("/Users/abichevo/PycharmProjects/APIautomation/GETrequest/post-request.rtf", "r+")



@pytest.mark.skipif(a>100, reason = "Condition is not satisfied")
def test_create_new_user(start_exec):
    # Read Json Input file
    json_input = file.read()
    request_json = json.loads(json_input)
    # make post request with json input body
    response = requests.post(url, request_json)
    # Validating response code
    assert response.status_code == 201

@pytest.mark.Smoke
def test_create_other_user(start_exec):
    # Read Json Input file
    json_input = file.read()
    request_json = json.loads(json_input)
    # make post request with json input body
    response = requests.post(url, request_json)
    # Validating response code
    assert response.status_code == 201
    # Fetch header from response
    print(response.headers.get("Content-length"))
    # Parse response to Json format
    response_json = json.loads(response.text)
    # Pick ID using Json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
