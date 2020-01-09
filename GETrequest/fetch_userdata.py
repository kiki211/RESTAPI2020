import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

# Send get URL
response = requests.get(url)

#Parse response to json format
json_response = json.loads(response.text)
print (json_response)

# Fetch value using json path
pages = jsonpath.jsonpath(json_response, "total_pages")
print("The result is: " + str(pages[0]))

assert pages[0] == 2



