import base64
import requests

def get_spotify_access_token(client_id, client_secret):
    # Concatenate client ID and client secret and encode in base64
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")

    # Spotify Accounts service endpoint for obtaining access tokens
    token_url = "https://accounts.spotify.com/api/token"

    # Set headers and data for the token request
    headers = {
        "Authorization": f"Basic {credentials}",
    }
    data = {
        "grant_type": "client_credentials",
    }

    # Make a POST request to obtain the access token
    response = requests.post(token_url, headers=headers, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to extract the access token
        access_token = response.json().get("access_token")
        return access_token
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Replace these with your own client ID and client secret
client_id = "fedb386c560e4c029c93cff5c2a5ad2f"
client_secret = "eb5589d692334487a5efa91c7a0b9214"

# Get the Spotify API access token
access_token = get_spotify_access_token(client_id, client_secret)

# Print the access token
print(f"Spotify API Access Token: {access_token}")
