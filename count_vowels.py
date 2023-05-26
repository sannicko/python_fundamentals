
user_input = input("Please enter a word: ")

count = 0

vowels = "AEIUOaeiou"
vowel_output = " "

for char in user_input:
  if char in vowels:
    vowel_output += char
    count = count + 1
    
print ("There are", str(count), "vowels in the word", "\"", user_input, "\"")
print ("The vowels are:", vowel_output)