import requests
import json

fedex_url = "https://apis.fedex.com/"

auth_url = fedex_url+"oauth/token"
auth_input = {
    'grant_type': 'client_credentials',
    'client_id': 'l7277fd88307004a7fb0878d55f17649e9',
    'client_secret': '91bb6c90813c4338a26f6eb9d44c311a'
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
            "trackingNumber": "776947146685"
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
tracking_dict = json.loads(track_response.text)
print(json.dumps(tracking_dict, indent=4, sort_keys=True))
