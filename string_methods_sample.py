
# string Methods: stripping
# stripping methods return a copy of a string with the leading and/or trailing characters removed

# strip()	removes both leading and trailing white spaces

user_input = input("Please enter a word: ")
user_input = user_input.strip()  # remove leading and trailing whitespace

count = 0
vowels = "AEIOUaeiou"

for char in user_input:
    if char in vowels:
        print(char)
        count += 1

print("There are", count, "vowels in the word", "\"", user_input, "\"")


# lstrip()	removes leading left white spaces	
# by using lstrip(), you can handle cases where the user accidentally enters extra spaces at the beginning of the input, making the program more robust.
 
city = ' San Francisco '
print(city) # without lstrip method
print(city.lstrip()) # # remove leading whitespace

# rstrip()	removes leading right white spaces	
# using rstrip() ensures that any extra spaces or newline characters at the end of the input are removed before further processing, making the program more robust.
 
city1 = ' North Carolina   '
print(city1) # without rstrip method
print(city1.rstrip()) # remove trailing whitespace

