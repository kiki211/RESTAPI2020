import requests
import json
import jsonpath

def test_add_new_student():
    global id
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/Users/abichevo/PycharmProjects/APIautomation/adding_student", 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    print("Posted data: " + response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_get_details():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(API_URL)
    print(response.text)



