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
    if(len(artist_name)==0):
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
    if(len(artist_id)==0):
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

def value_checker(list):
    if(list is None or len(list) == 0):
        return False
    else:
        return True

print("Hi, I'm Py. I will help you to search the song or artist on spotify")
user_input=input("Enter if you want to look for Artist or Song ")
confirm=1
while(confirm!=0):
    if(user_input.lower()=="artist"):
        artist_name=input("Enter the name of Artist")
        artist_values=search_artist(get_token(),artist_name)
        flag=1
        while(flag!=0):
            if(value_checker(artist_values)):
                print("Here are the details of the artist")
                print("These are the top tracks of the artist about you asked")
                artist_id=artist_values[0]['id']
                result = top_tracks_artist(get_token(), artist_id)
                for x in range(0, len(result)):
                  print(f"{x+1} {result[x]['name']}")
                break


            else:
                print("Sorry the Artist's name you entered doesn't exist.")
                checker=input("Do you want to search again? Please enter Yes or No")
                while(checker!="no" or checker!="yes"):
                    print("Please enter the valid input")
                    checker = input("Please enter Yes or No")
                if(checker.lower()=="no"):
                    flag=0
    confirming=input("Do you still want to search anything? Yes or No")
    while (confirming != "no" or confirming != "yes"):
        print("Please enter the valid input")
        confirming = input("Please enter Yes or No")
        if(confirming.lower()=="no"):
            confirm=0
