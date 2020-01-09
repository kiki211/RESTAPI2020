import requests
import json

#API URL
url = "https://reqres.in/api/users"

# Read Json Input file
file = open("../GETrequest/post-request.rtf", "r+")
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)

# make post request with json input body
response = requests.post(url, request_json)
print(response.content)

# Validating response code
print(response.status_code)
assert response.status_code == 201

