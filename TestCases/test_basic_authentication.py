import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get("https://api.github.com/user", auth = HTTPBasicAuth('kiki211', 'KseniBi211'))
    print(response.text)

# Generating access token oAuth. Send creds and server responnses with token.

