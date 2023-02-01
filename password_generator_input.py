import string
import random

# 9 characters in length and special one

# def generate_password():
  
#   # mixing characters and digits
#   char1 = random.choice(string.ascii_letters)
#   char2 = random.randint(0,9)
#   char3 = random.choice(string.ascii_letters)
#   char4 = random.randint(0,9)
#   char5 = random.choice(string.punctuation)
#   char6 = random.choice(string.ascii_letters)
#   char7 = random.randint(0,9)
#   char8 = random.choice(string.ascii_letters)
#   char9 = random.randint(0,9)
#   print ("Password =",char1,char2,char3,char4,char5,char6,char7,char8,char9)

# print(generate_password())

def generate_password2(letters, digits, special_char):
  for char in range (0, letters):
    print(random.choice(string.ascii_letters), end = " ")
  for char in range (0, digits):
    print(random.randint(0,9), end = " ")
  for char in range (0, special_char):
    print(random.choice(string.punctuation), end = " ")

# call function and ask user number of characters, digits and special characters

letter_num = int(input("How many letters in password?"))
digit_num = int(input("How many numbers in password?"))
special_char = int(input("How many special characters in password?"))

print(generate_password2(letter_num, digit_num, special_char))