# Syntax:

# for index, value in enumerate(list_name):
# 	# loop body
# To help index elements while iterating, the enumerate() function can be used to add a counter to each element of the list.


def flavor():
  # initialize an empty list to store the flavors
  flavors = [] 
   # use a while loop to keep asking the user for their favorite flavor until user type quit
  while True: 
        flavor = input("Enter your favorite flavor (or type 'quit' to quit): ").lower()
        # if statement to check if the user has entered 'quit'
        if flavor == 'quit':
            break
        flavors.append(flavor) # add each input to the list of flavors
  # the enumerate function to loop through the flavors list and print the index and value
  for index, val in enumerate(flavors):
      print(index, ":", val)
  return(flavors)


print (flavor())