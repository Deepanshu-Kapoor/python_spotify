import json
import os
import base64
from requests import post, get
from dotenv import load_dotenv

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
    if len(artist_name) == 0:
        return None
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
    json_result = json.loads(result.content)['artists']['items']

    # Return the parsed JSON result
    return json_result

def top_tracks_artist(token, artist_id):
    if len(artist_id) == 0:
        return None
    # Spotify API search endpoint
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=CA"

    # Get the authorization header with the access token
    header = get_auth_header(token)

    # Make a GET request to the Spotify API with the full URL and authorization header
    result = get(url, headers=header)

    # Parse the JSON response content
    json_result = json.loads(result.content)["tracks"]

    # Return the parsed JSON result
    return json_result

def search_album(token, album_name):
    if len(album_name) == 0:
        return None
    # Spotify API search endpoint
    url = "https://api.spotify.com/v1/search"

    # Get the authorization header with the access token
    header = get_auth_header(token)

    # Construct the query string with the artist name, search type, and result limit
    query = f"?q={album_name}&type=album&limit=1"

    # Combine the base URL and query string to form the full URL
    query_url = url + query

    # Make a GET request to the Spotify API with the full URL and authorization header
    result = get(query_url, headers=header)

    # Parse the JSON response content
    json_result = json.loads(result.content)['albums']['items']

    # Return the parsed JSON result
    return json_result

def tracks_album_items(token, album_id):
    if len(album_id) == 0:
        return None
    # Spotify API search endpoint
    url = f"https://api.spotify.com/v1/albums/{album_id}?country=CA"

    # Get the authorization header with the access token
    header = get_auth_header(token)

    # Make a GET request to the Spotify API with the full URL and authorization header
    result = get(url, headers=header)

    # Parse the JSON response content
    json_result = json.loads(result.content)["tracks"]["items"]

    # Return the parsed JSON result
    return json_result

def get_spotify_id(search_output):
    return search_output[0]["id"]