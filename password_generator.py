import string
import random

# generate password that is 8 characters in length
def generate_password():
  # first 4 characters are letters
  char1 = random.choice(string.ascii_letters)
  char2 = random.choice(string.ascii_letters)
  char3 = random.choice(string.ascii_letters)
  char4 = random.choice(string.ascii_letters)

  # last 4 characters are digits
  char5 = random.randint(0,9)
  char6 = random.randint(0,9)
  char7 = random.randint(0,9)
  char8 = random.randint(0,9)
  
   # last character is an special character
  char9 = random.choice(string.punctuation)

  # print random password
  print(char1, char2, char3, char4, char5, char6, char7, char8, char9)

# call & test function works
generate_password()