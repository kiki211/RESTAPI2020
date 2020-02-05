import requests
import json
import jsonpath
import pytest

def test_add_new_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('/Users/abichevo/PycharmProjects/APIautomation/post_request.txt', 'r')
    json_content = json.loads(f.read())
    response = requests.post(API_URL, json_content)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])


    # UPdating technical details
    API_URL = "http://thetestingworldapi.com/api/technicalskills"
    f = open("/Users/abichevo/PycharmProjects/APIautomation/technical_skills", 'r')
    request_json = json.loads(f.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    print(request_json)
    response = requests.post(API_URL,request_json)
    back_end_response = response
    print(back_end_response.text)

    #Updating address
    API_URL = "http://thetestingworldapi.com/api/addresses"
    f = open("/Users/abichevo/PycharmProjects/APIautomation/address_upload", 'r')
    json_content = json.loads(f.read())
    request_json['stId'] = id[0]
    response = requests.post(API_URL, json_content)
    #print(response.text)

    #Geting final student details
    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(final_details)
    print(response.text)


test_add_new_data()