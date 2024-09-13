# Importing necessary functions from model and view
from model import get_token, search_artist, top_tracks_artist, get_spotify_id, search_album, tracks_album_items
from view import value_checker, continue_or_not, display_artist_details, display_album_details


# Main function that serves as the entry point to the program
def main():
    # Greeting and prompt for user input
    print("Hi, I'm Py. I will help you to search the album or artist on Spotify.")
    user_input = input("Enter if you want to look for Artist or Album: ").strip().lower()

    # Validate user input (it should be 'artist' or 'album')
    if user_input in ["artist", "album"]:
        confirm = 1  # Valid input, proceed with the program
    else:
        confirm = 0  # Invalid input
        print("Please enter a valid input")  # Notify the user about invalid input

    # Main loop to keep the program running until user chooses to exit
    while confirm != 0:
        if user_input == "artist":
            flag1 = 1  # Flag to control the artist search loop
            while flag1 != 0:
                # Prompt user to input the artist's name
                artist_name = input("Please enter the name of the artist: ").strip()
                # Search for the artist using the Spotify API
                artist_values = search_artist(get_token(), artist_name)

                # Check if the artist is found
                if value_checker(artist_values):
                    # Display the artist details
                    display_artist_details(artist_values)
                    # Get the artist ID for fetching top tracks
                    artist_id = get_spotify_id(artist_values)
                    # Fetch and display the top tracks of the artist
                    result = top_tracks_artist(get_token(), artist_id)
                    display_artist_details(result)
                else:
                    # Artist not found, prompt user to try again
                    print("Sorry, the artist's name you entered doesn't exist.")
                    flag1 = continue_or_not("Do you want to search again? Please enter Yes or No: ")

                # Ask if the user wants to search for another artist
                if flag1 != 0:
                    flag1 = continue_or_not("Do you still want to search another artist? Yes or No: ")
                    if flag1 == 0:
                        break  # Exit the artist search loop if user chooses not to search further

        elif user_input == "album":
            flag2 = 1  # Flag to control the album search loop
            while flag2 != 0:
                # Prompt user to input the album's name
                album_name = input("Please enter the name of the album: ").strip()
                # Search for the album using the Spotify API
                result = search_album(get_token(), album_name)

                # Check if the album is found
                if value_checker(result):
                    # Get the album ID for fetching album tracks
                    album_id = get_spotify_id(result)
                    # Fetch and display the tracks in the album
                    album_items = tracks_album_items(get_token(), album_id)
                    display_album_details(album_items, result)
                else:
                    # Album not found, prompt user to try again
                    print("Sorry, the album's name you entered doesn't exist.")
                    flag2 = continue_or_not("Do you want to search again? Please enter Yes or No: ")

                # Ask if the user wants to search for another album
                flag2 = continue_or_not("Do you still want to search another album? Yes or No: ")

        else:
            # If the input was neither 'artist' nor 'album'
            print("Wrong input Please enter the correct input.")

        # Ask the user if they want to search for another artist or album
        confirm = continue_or_not("Do you want to search for artist or album again? Yes or No: ")

        # If the user wants to continue, ask again whether to search for an artist or album
        if (confirm != 0):
            user_input = input("Enter if you want to look for Artist or Album: ").strip().lower()

    # Exit message
    print("Have a great day :)")


# Check if the script is being run directly (not imported) and call the main function
if __name__ == "__main__":
    main()
