import requests
import json
import jsonpath
import pytest

@pytest.mark.Smoke
def test_add_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/Users/abichevo/PycharmProjects/APIautomation/post_request.txt", "r+")
    json_request = json.loads(file.read())
    print(json_request)
    response = requests.post(API_URL, json_request)
    print(response.text)

test_add_student_data()


def test_put_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/154998"
    file = open("/Users/abichevo/PycharmProjects/APIautomation/post_request.txt", "r+")
    json_request = json.loads(file.read())
    print(json_request)
    update = requests.put(API_URL, json_request)
    print(update.text)

test_put_student_data()

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/154998"
    response = requests.get(API_URL)
    print("Get response is here: " + str(response.text))
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response,"data.id")
    print(id)
    assert id[0] == 154998


test_get_student_data()

def test_delete_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/154998"
    response = requests.get(API_URL)
    print(response.text)

test_delete_student()








