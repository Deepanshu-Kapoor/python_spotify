def value_checker(input_list):
    if input_list is None or len(input_list) == 0:
        return False
    else:
        return True

def continue_or_not(dialogue):
    # Prompt the user for input
    checker = input(dialogue).strip().lower()

    # Check if the input is either "yes" or "no"
    while checker not in ["no", "yes"]:
        print("Please enter a valid input.")
        checker = input("Please enter Yes or No: ").strip().lower()

    # Return 0 if the user enters "no", otherwise return 1
    if checker == "no":
        return 0
    else:
        return 1


def display_artist_details(artist_values):
    print("Here are the details of the artist")
    print("These are the top tracks of the artist you asked about:")
    for x in range(len(artist_values)):
        print(f"{x + 1} {artist_values[x]['name']}")

def display_album_details(values,output):
    print("Here are the details of the song")
    total_tracks=output[0]['total_tracks']
    print(f"This album have total {total_tracks} tracks.")
    print("These are the top tracks of the album you asked about:")
    for x in range(total_tracks):
        print(f"{x + 1} {values[x]['name']}")
