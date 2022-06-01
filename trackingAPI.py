import requests, json, config

tracking_number = "777001279771"


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
    auth_response = requests.request("POST", auth_url, data=auth_payload, headers=auth_headers)
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
    track_response = requests.request("POST", track_url, data=track_input, headers=track_headers)
    tracking_dict = json.loads(track_response.text)  # Make dictionary out of json response
    print("FedEx " + track_headers["Authorization"])
    print(json.dumps(tracking_dict["output"]["completeTrackResults"][0]["trackResults"][0]["scanEvents"], indent=4))


track(tracking_number)
