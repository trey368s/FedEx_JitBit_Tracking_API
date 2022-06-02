from requests.auth import HTTPBasicAuth
import config
import json
import requests
from datetime import datetime


def getTicketsList():
    jitbit_url = "https://shsupport.jitbit.com/helpdesk/api/tickets?mode=handledbyme&count=300"
    # JitBit Helpdesk API Documentation
    # https://www.jitbit.com/helpdesk/helpdesk-api/#/
    jitbit_auth = HTTPBasicAuth(config.JitBit_Username, config.JitBit_Password)  # Basic authorization headers
    jitbit_response = requests.get(url=jitbit_url, auth=jitbit_auth)
    tickets = json.loads(jitbit_response.content)  # All assigned tickets information
    print(jitbit_auth)
    assigned_tickets_list = []
    for x in range(len(tickets)):  # Go through list of tickets and make an array of ticket numbers
        assigned_tickets_list.append(json.dumps(tickets[x]["IssueID"]))
    return assigned_tickets_list  # Return list of assigned tickets


def getTrackingNumber(ticket_number):
    jitbit_url = "https://shsupport.jitbit.com/helpdesk/api/ticket?id=" + str(ticket_number)
    jitbit_auth = HTTPBasicAuth(config.JitBit_Username, config.JitBit_Password)  # Basic authorization headers
    jitbit_response = requests.get(url=jitbit_url, auth=jitbit_auth)
    ticket = json.loads(jitbit_response.content)  # Tickets detailed information
    return str(json.dumps(ticket["Tags"][0]["Name"])[1:-1])  # Return ticket's tag


def track(tracking_number):
    fedex_url = "https://apis.fedex.com/"
    # FedEx Authorization API Documentation
    # https://developer.fedex.com/api/en-us/catalog/track/docs.html
    auth_url = fedex_url + "oauth/token"
    auth_payload = {
        'grant_type': 'client_credentials',
        'client_id': config.API_KEY,  # Public key
        'client_secret': config.API_SECRET  # Secret key
    }
    auth_headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }
    auth_response = requests.request("POST", url=auth_url, data=auth_payload, headers=auth_headers)
    response_dict = json.loads(auth_response.text)  # Turn json response into dictionary
    access_token = response_dict['access_token']  # Get bearer token out of response dictionary
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
        'Authorization': "Bearer " + access_token  # Adds  bearer access token to header for authentication
    }
    track_response = requests.request("POST", url=track_url, data=track_input, headers=track_headers)
    tracking_dict = json.loads(track_response.text)  # Make dictionary out of json response
    print("FedEx " + track_headers["Authorization"])
    return json.dumps(tracking_dict["output"]["completeTrackResults"][0]["trackResults"][0], indent=4)  # Get scan events


def createTrackingUpdate(track_info):
    scan_events = json.loads(track_info)
    time = datetime.strptime(scan_events["scanEvents"][0]['date'].split('T')[1][0:5], "%H:%M")
    print("AUTOMATED TRACKING UPDATE: " +
          scan_events["scanEvents"][0]['eventDescription'] + " in " +
          scan_events["scanEvents"][0]['scanLocation']['city'].title() + ", " +
          scan_events["scanEvents"][0]['scanLocation']['stateOrProvinceCode'] + " at " +
          time.strftime("%I:%M%p") + " " +
          scan_events["scanEvents"][0]['date'].split('T')[0] + ".")


getTicketsList()
createTrackingUpdate(track(getTrackingNumber(48524901)))

