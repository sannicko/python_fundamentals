
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


# The string methods for splitting allow you to break a string into multiple parts based on a specified delimiter or pattern. Below are some commonly used string methods for splitting:

# The split() method is a string method in Python that is used to split a string into a list of substrings based on a specified delimiter. It divides the string at each occurrence of the delimiter and returns the resulting substrings as a list.

# Syntax: string.split(delimiter, maxsplit)
# The delimiter parameter specifies the character or substring at which the string should be split. If no delimiter is specified, the split() method splits the string at whitespace characters (spaces, tabs, and newlines) by default.
# The maxsplit parameter is an optional parameter that specifies the maximum number of splits to be performed. If maxsplit is specified, the string is split at most maxsplit - 1 times, and the remaining part of the string is returned as the last element in the list.
# The split() method returns a list of substrings resulting from the split operation.
# The original string is not modified; the split() method returns a new list.


city_str = "The Bronx, New York"

# split at the default delimiter (whitespace)
city_list = city_str.split()
print(city_list)  # output: ['The', 'Bronx,', 'New', 'York']

# split at a specific delimiter (",")
parts = city_str.split(",")
print(parts)  # output: ['The Bronx', ' New York']

# split at a specific delimiter ("o") with maxsplit
fragments = city_str.split("o", 2)
print(fragments)  # output: ['The Br', 'nx, New Y', 'rk']

# splitting a string with multiple delimiters
date = "2022-05-22"
components = date.split("-")
print(components)  # Output: ['2022', '05', '22']


# The string methods: Joining
# The join() method returns a string in which the elements of the sequence have been joined by a separator.
# It's also used to concatenate elements of an iterable (such as a list or tuple) into a single string, using a specified separator. It takes the form of 'separator'.join(iterable).


sentence = "Today is a 29 day of May"
separator = "#"
number = separator.join(sentence.split())
print(number)

fruit_list = ['orange', 'red berry', 'blue berry', 'apple']
separator = " | "
new_fruit_list = separator.join(fruit_list)
print(new_fruit_list)

# You can customize the separator to any string you prefer, such as ',', '-', '|' or even an empty string '' for concatenation without any separator. The join() method provides a flexible way to join elements of an iterable into a single string with the desired formatting.

