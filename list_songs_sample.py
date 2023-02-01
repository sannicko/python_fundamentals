def song_request_manager():
    # Print a welcome message
    print("Welcome to the Song Request Manager")
    print("Enter the song title to make a request.")
    print("To exit, enter 'Quit'.")

    # Initialize an empty list to store song requests
    song_list = []

    # Use a while loop to continuously ask for song titles
    while True:
        # Get the song title and convert it to lowercase
        song_title = input("\nEnter a song title: ").lower()

        # Check if the user entered 'quit'
        if song_title == "quit":
            # Print a goodbye message and the list of song requests
            print("Bye Bye, enjoy your songs")
            print(song_list)
            # Break out of the loop
            break

        # Check if the song title is already in the list of song requests
        if song_title in song_list:
            # Print a message indicating the song has already been requested
            print(f"The song '{song_title}' has already been requested.")
            print(f"It is song number {song_list.index(song_title) + 1} on the list!")
        else:
            # Add the song title to the list of song requests
            song_list.append(song_title)
            # Print a message indicating the song has been added to the list
            print(f"The song '{song_title}' has been added to the list.")
            print(f"It is song number {len(song_list)} on the list.")

# Call the function to run the song request manager
song_request_manager()