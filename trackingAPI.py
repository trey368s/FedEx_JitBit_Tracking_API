import base64

from requests.auth import HTTPBasicAuth

import config
import json
import requests

tracking_number = "776958984516"


def track(tracking_number):
    fedex_url = "https://apis.fedex.com/"
    # FedEx Authorization API Documentation
    # https://developer.fedex.com/api/en-us/catalog/track/docs.html
    auth_url = fedex_url + "oauth/token"
    auth_input = {
        'grant_type': 'client_credentials',
        'client_id': config.API_KEY,  # Public key
        'client_secret': config.API_SECRET  # Secret key
    }
    auth_payload = auth_input
    auth_headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }
    auth_response = requests.request("POST", url=auth_url, data=auth_payload, headers=auth_headers)
    response_dict = json.loads(auth_response.text)
    access_token = response_dict['access_token']  # Get bearer token out of json response
    # FedEx Track API Documentation
    # https://developer.fedex.com/api/en-us/catalog/track/docs.html
    track_url = fedex_url + "track/v1/trackingnumbers"
    track_input = json.dumps({
        "includeDetailedScans": True,
        "trackingInfo": [
            {
                "trackingNumberInfo": {
                    "trackingNumber": tracking_number
                }
            }
        ]
    })
    track_headers = {
        'Content-Type': "application/json",
        'X-locale': "en_US",
        'Authorization': "Bearer " + access_token  # Adds access token to header for authorization
    }
    track_response = requests.request("POST", url=track_url, data=track_input, headers=track_headers)
    tracking_dict = json.loads(track_response.text)  # Make dictionary out of json response
    print("FedEx " + track_headers["Authorization"])
    print(json.dumps(tracking_dict["output"]["completeTrackResults"][0]["trackResults"][0]["scanEvents"], indent=4))


def getTickets():
    jitbit_url = "https://shsupport.jitbit.com/helpdesk/api/tickets?mode=handledbyme&count=300"
    jitbit_auth = HTTPBasicAuth(config.JitBit_Username, config.JitBit_Password)
    jitbit_response = requests.get(url=jitbit_url, auth=jitbit_auth)
    tickets = json.loads(jitbit_response.content)
    print(jitbit_auth)
    print(json.dumps(tickets, indent=4))
    assigned_tickets_list = []
    for x in range(len(tickets)):
        assigned_tickets_list.append(json.dumps(tickets[x]["IssueID"]))
    print(assigned_tickets_list)


track(tracking_number)
getTickets()
