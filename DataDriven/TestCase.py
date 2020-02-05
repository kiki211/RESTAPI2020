import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library



# Implementing data driven test case
def test_add_multiple_students():
    # Add one student
    ap_url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('/Users/abichevo/PycharmProjects/APIautomation/post_request.txt', 'r')
    json_request = json.loads(f.read())

    # Excel code: add multiple students from Excel sheet
    obj = Library.Common('/Users/abichevo/PycharmProjects/APIautomation/mult_students.xlsx', 'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keylist = obj.fetch_key_names()


    for i in range(2, row+1):
        updated_json_request = obj.update_request_with_data(i, json_request, keylist)
        response = requests.post(ap_url, updated_json_request)
        print(response)
        assert response.status_code == 201

# new comment


