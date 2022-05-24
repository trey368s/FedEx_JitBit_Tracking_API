import requests
import json
import pprint

fedex_url = "https://apis-sandbox.fedex.com/"

auth_url = fedex_url+"oauth/token"
auth_input = {
    'grant_type': 'client_credentials',
    'client_id': 'l745348f4bffe544988058d45686377aa4',
    'client_secret': '29470d65a125454b95d0607468a9dcb9'
}
auth_payload = auth_input
auth_headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }
auth_response = requests.request("POST", auth_url, data=auth_payload, headers=auth_headers)
response_dict = json.loads(auth_response.text)
access_token = response_dict['access_token']

track_url = fedex_url+"track/v1/associatedshipments"
track_input = json.dumps({
    "associatedType": "STANDARD_MPS",
    "masterTrackingNumberInfo": {
        "trackingNumberInfo": {
            "trackingNumber": "122816215025810"
            }
    }
})
track_headers = {
    'Content-Type': "application/json",
    'X-locale': "en_US",
    'Authorization': "Bearer " + access_token
    }
track_response = requests.request("POST", track_url, data=track_input, headers=track_headers)
print(track_headers)
pprint.pprint(track_response.text)
