from model import get_token, search_artist, top_tracks_artist, get_spotify_id, search_album, tracks_album_items
from view import value_checker, continue_or_not, display_artist_details, display_album_details

def main():
    print("Hi, I'm Py. I will help you to search the album or artist on Spotify.")
    user_input = input("Enter if you want to look for Artist or Album: ").strip().lower()

    if user_input in ["artist", "album"]:
        confirm = 1
    else:
        confirm = 0
        print("Please enter a valid input")

    while confirm != 0:
        if user_input == "artist":
            flag1 = 1
            while flag1 != 0:
                artist_name = input("Please enter the name of the artist: ").strip()
                artist_values = search_artist(get_token(), artist_name)
                if value_checker(artist_values):
                    display_artist_details(artist_values)
                    artist_id = get_spotify_id(artist_values)
                    result = top_tracks_artist(get_token(), artist_id)
                    display_artist_details(result)
                else:
                    print("Sorry, the artist's name you entered doesn't exist.")
                    flag1 = continue_or_not("Do you want to search again? Please enter Yes or No: ")

                if flag1 != 0:
                    flag1 = continue_or_not("Do you still want to search another artist? Yes or No: ")
                    if flag1 == 0:
                        break

        elif user_input == "album":
            flag2 = 1
            while flag2 != 0:
                album_name = input("Please enter the name of the album: ").strip()
                result = search_album(get_token(), album_name)
                if value_checker(result):
                    album_id = get_spotify_id(result)
                    album_items = tracks_album_items(get_token(), album_id)
                    display_album_details(album_items, result)
                else:
                    print("Sorry, the album's name you entered doesn't exist.")
                    flag2 = continue_or_not("Do you want to search again? Please enter Yes or No: ")


                flag2 = continue_or_not("Do you still want to search another album? Yes or No: ")

        else:
            print("Wrong input Please enter the correct input.")
        confirm = continue_or_not("Do you want to search for artist or album again? Yes or No: ")
        if(confirm!=0):
            user_input = input("Enter if you want to look for Artist or Album: ").strip().lower()

    print("Have a great day :)")

if __name__ == "__main__":
    main()
