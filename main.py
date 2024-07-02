import json
from dotenv import load_dotenv
import os
import base64

from requests import post,get

# Load environment variables from .env file
load_dotenv()

# Fetch client ID and client secret from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# Function to get a temporary access token from Spotify API
def get_token():
    # Combine client ID and client secret into a single string
    auth_string = client_id + ":" + client_secret

    # Encode the combined string into bytes
    auth_bytes = auth_string.encode("utf-8")

    # Base64 encode the bytes and decode into a string
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    # Spotify API token endpoint
    url = "https://accounts.spotify.com/api/token"

    # Headers for the POST request including the Authorization header
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Data payload for the POST request
    data = {"grant_type": "client_credentials"}

    # Make a POST request to the token endpoint
    result = post(url, headers=headers, data=data)

    # Parse the response JSON to get the access token
    json_result = json.loads(result.content)
    token = json_result['access_token']

    # Return the access token
    return token


# Function to create authorization headers using the access token
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


# Function to search for an artist using the Spotify API
def search_artist(token, artist_name):
    # Spotify API search endpoint
    url = "https://api.spotify.com/v1/search"

    # Get the authorization header with the access token
    header = get_auth_header(token)

    # Construct the query string with the artist name, search type, and result limit
    query = f"?q={artist_name}&type=artist&limit=1"

    # Combine the base URL and query string to form the full URL
    query_url = url + query

    # Make a GET request to the Spotify API with the full URL and authorization header
    result = get(query_url, headers=header)

    # Parse the JSON response content
    json_result = json.loads(result.content)

    # Return the parsed JSON result
    return json_result


print(search_artist(get_token(),"Karan Aujla"))
print("Hi, I'm Py. I will help you to search the song or album of an artist or even if you don't know artist")
user_input=input("Enter the ");
def search_by_artist(artist_name):

    return True
