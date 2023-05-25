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

allowed_special_chars = ['!', '(', ')', '-', '.', '?', '[', ']', '_', '`', '~', ';', ':', '#', '$', '%', '^', '&', '*', '+', '=']

# this function could repeat the same letters consecutive when generating the password

def generate_password2(letters, digits, special_chars):
  password = ''  # initializes the variable as an empty string
  for char in range (letters):
    password += random.choice(string.ascii_letters)
  for char in range (digits):
    password += str(random.randint(0,9))
  for char in range (special_chars):
    password += random.choice(allowed_special_chars)
  return password


# this function does not repeat the same letters consecutive when generating the password

def generate_password3(letters, digits, special_chars):
    password = ''
    previous_char = ''
    
    for char in range(letters):
        current_char = random.choice(string.ascii_letters)
        
        while current_char == previous_char:
            current_char = random.choice(string.ascii_letters)
        
        password += current_char
        previous_char = current_char
    
    for char in range(digits):
        password += str(random.randint(0, 9))
    
    for char in range(special_chars):
        password += random.choice(allowed_special_chars)
    
    return password


# call function and ask user number of characters, digits and special characters

letter_num = int(input("How many letters in password?"))
digit_num = int(input("How many numbers in password?"))
special_chars = int(input("How many special characters in password?"))

print(generate_password2(letter_num, digit_num, special_chars))
print(generate_password3(letter_num, digit_num, special_chars))