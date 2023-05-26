def song_request_manager():
    # print a welcome message
    print("Welcome to the Song Request Manager")
    print("Enter the song title to make a request.")
    print("To exit, enter 'Quit'.")

    # initialize an empty list to store song requests
    song_list = []

    # use a while loop to continuously ask for song titles
    while True:
        # get the song title and convert it to lowercase
        song_title = input("\nEnter a song title: ").lower()

        # check if the user entered 'quit'
        if song_title == "quit":
            # print a goodbye message and the list of song requests
            print("Bye Bye, enjoy your songs")
            print(song_list)
            # break out of the loop
            break

        # check if the song title is already in the list of song requests
        if song_title in song_list:
            # print a message indicating the song has already been requested
            print(f"The song '{song_title}' has already been requested. Please choose another song.")
            print(f"It is song number {song_list.index(song_title) + 1} on the list!")
        else:
            # add the song title to the list of song requests
            song_list.append(song_title)
            # print a message indicating the song has been added to the list
            print(f"The song '{song_title}' has been added to the list.")
            print(f"It is song number {len(song_list)} on the list.")

# call the function to run the song request manager
song_request_manager()