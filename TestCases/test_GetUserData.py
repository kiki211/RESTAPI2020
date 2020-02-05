import requests
import json
import jsonpath
import pytest


@pytest.mark.Sanity
def test_fetch_user_details():
    #API URL
    url = "https://reqres.in/api/users?page=2"
    #Send get request
    response = requests.get(url)
    #Parse response to Json format
    json_response = json.loads(response.text)
    # Fetch value using json path
    for i in range(0,3):
        first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
        print((first_name[0]))


