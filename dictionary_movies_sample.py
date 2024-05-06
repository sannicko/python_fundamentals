current_movies = {"Dark Night" : "1:00pm",
                  "Jurasic Park" : "2:00pm",
                  "Babilon" : "3:00pm",
                  "Night Love" : "4:00pm",
                  "Web" : "5:00pm",}

print("These are the current movies:")
for key in current_movies:
  print(str(list(current_movies.keys()).index(key) + 1) + ". " + key)

movie = input("Select the movie to see the showtime ")

showtime = current_movies.get(movie)

if showtime == None:
  print("Select one of the current movie")
else:
  print("The movie: ", movie, "starts at", showtime)