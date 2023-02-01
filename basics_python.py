# print basic text, call print function and the string inside ""

#print("hello world")


# to type an input, call input function 
# answer = input("Whats your name?")
# print("Hello", answer)


# answer = input ("Welcome to this game, please type your name: ")
# print("Hello", answer)
# print("Please type the below four worlds ")
# adjective = input ("Please enter an adjective: ")
# noun = input ("Please enter an noun: ")
# animal = input ("Please enter an animal: ")
# sound = input ("Please enter an sound: ")
# print("When the", adjective, "arrived", noun, "the human was bite by the", animal, "and make a", sound)

#  program using conditional if and elif that will ask the user what their grade is and output their associated letter grade.

# grade = input ("Type grade from 10 to 100:   ")

# grade = int(grade) # convert the user's input from strig type to integer, using the int() function

# if grade > 90:
#   print("your grade is: A")
# elif grade > 80:
#   print("your grade is: B")	
# elif grade > 70:
#   print("your grade is: C")
# elif grade >= 65:
#   print("your grade is: D")
# else:
#   print("your grade is: F retake the class")

# function to convert feet to meters
# def feet_to_meters(feet):
#   return 0.3048 * feet
# feet = input ("Type the feets to convert them into meters: ")
# feet = int(feet)
# feet = {feet_to_meters(feet)}
# print(feet)

# # Ask the user what color the animal is
# color = input("What color is your animal's fur/skin?")

# # Ask the user how tall the animal is
# height = input("How tall is your animal in feet?")

# # We need to convert height into an integer type
# height = int(height)

# # Check if the color is yellow
# if color == "yellow":
#   # If color is yellow, we know that the animal is either a giraffe or tiger.
#   # Next, check the height of the animal

#   if height == 10:
#     print("It's a giraffe!")
#   elif height >= 3:
#     print("It's a tiger")
#   else:
#       print("I do not know")
# else:
#   # if color is not yellow, we know the animal is either an elephant or monkey
#   # Next, check the height of the animal

#   if height < 10:
#     print("It's a monkey!")
#   else:
#     print("It's an elephant")


# # If the color is NOT yellow, check if it is an elephant or monkey


# Definin a Function Syntax

# def func_name(parm1, param2): function signature
 # doSomething # function body
 # return result
 
#  # Defining the university_standing function
# def university_standing (grad_year):
#   if grad_year == 2022:
#     return "senior"
#   elif grad_year == 2023:
#     return "junior"
#   elif grad_year == 2024:
#     return "sophomore"
#   elif grad_year <= 2025:
#     return "freshman"
#   else:
#     return "alumni"

# # Defining variable year and setting to value 2023 to test
# year = input("Type a year between 2022 and 2025?")
# year = int(year)
# # Calling function university_standing with input year
# university_standing(year)
# print("Peter is",university_standing(year))

# # global variable
# secret_number = 13

# def guess_number (guess):
#   if (guess < secret_number):
#     return "guess is higher"
#   elif (guess > secret_number):
#     return "guess is lower"      
#   else:
#     return "guess is correct"

# # call the function
# guess = input ("Guess what the secret number is:  ")
# guess = int(guess)
# result = guess_number(guess)
# print(result)

# global variable
secret_number = 13
def guess_number (guess):
  while secret_number!= guess:
    if (guess < secret_number):
      print ("guess is higher")
      guess = int(input("Try again: "))
    elif (guess > secret_number):
      print ("guess is lower")      
      guess = int(input("Try again: "))
    else:
      break
  print ("you found the number") 

# call the function
guess = input ("Guess what the secret number is:  ")
guess = int(guess)
result = guess_number(guess)
print(guess)
