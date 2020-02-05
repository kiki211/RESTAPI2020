import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users/2"

# Read Json Input file
file = open("../GETrequest/post-request.rtf", "r+")
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)

# make PUT request with json input body
response = requests.put(url,request_json)

# Validating response code
print(response.status_code)
assert response.status_code == 200

# Parse response Content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json,"updatedAt")
print(updated_li[0])