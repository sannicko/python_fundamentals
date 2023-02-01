# Import libraries
import random

# global variable
secret_number = random.randint(1,10)

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
  print ("you found the number", guess) 

# call the function
guess = input ("Guess what the secret number is:  ")
#guess = int(guess)
result = guess_number(int(guess))
print(result)