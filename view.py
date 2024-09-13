# Function to check if the input list is valid (not None and not empty)
def value_checker(input_list):
    if input_list is None or len(input_list) == 0:
        return False  # Return False if the list is None or empty
    else:
        return True  # Return True if the list contains valid items


# Function to prompt the user to continue or not (expects a 'Yes' or 'No' response)
def continue_or_not(dialogue):
    # Prompt the user for input based on the provided dialogue
    checker = input(dialogue).strip().lower()

    # Check if the input is either "yes" or "no"
    while checker not in ["no", "yes"]:
        print("Please enter a valid input.")  # If input is invalid, prompt again
        checker = input("Please enter Yes or No: ").strip().lower()

    # Return 0 if the user enters "no", otherwise return 1
    if checker == "no":
        return 0  # User doesn't want to continue
    else:
        return 1  # User wants to continue


# Function to display the details of an artist (showing their top tracks)
def display_artist_details(artist_values):
    print("Here are the details of the artist")
    print("These are the top tracks of the artist you asked about:")

    # Loop through the artist's top tracks and display them
    for x in range(len(artist_values)):
        print(f"{x + 1} {artist_values[x]['name']}")  # Display track number and name


# Function to display the details of an album (showing its tracks)
def display_album_details(values, output):
    print("Here are the details of the album")

    # Fetch the total number of tracks in the album
    total_tracks = output[0]['total_tracks']
    print(f"This album has a total of {total_tracks} tracks.")

    # Display the top tracks of the album
    print("These are the top tracks of the album you asked about:")
    for x in range(total_tracks):
        print(f"{x + 1} {values[x]['name']}")  # Display track number and name
