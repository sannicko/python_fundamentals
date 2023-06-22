# this code checks if a word is a palindrome by comparing characters from both ends of the word towards the middle. If at any point the characters don't match, it determines that the word is not a palindrome. If the entire word has been checked and all the characters match, it determines that the word is a palindrome.

# code breakdown
# the variables pointer1 and pointer2 are defined to be used as pointers.
# pointer1 is initialized to 0 which is the leftmost index of the string.
# pointer2 is initialized to len(str)-1 which is the rightmost (last) index of the string.
# then using the while loop, the program will iterate through the string as long as the index of pointer1 is less than the index of pointer2.
# inside the loop, there exists a condition that checks if the character pointer1 is referencing is not equivalent to the character pointer2 is a reference. If the characters are not equivalent, the string is not a palindrome and False is returned.
# in the cases where the characters are equivalent, pointer1 is incremented by 1, giving it an index value of the next character to the right. pointer2 is decremented by 1, giving it an index value of the next character to the left.
# after the loop finished iterating and comparing each pair of characters, it can be assumed that the palindrome conditions were met and the program returns True.

def is_palindrome(word):
  pointer1 = 0
  pointer2 = len(word)-1
  
  while pointer1 < pointer2:
    if word[pointer1] != word[pointer2]:
      return ("False: " + word + " is not palindrome word")
    pointer1 += 1
    pointer2 -= 1
    
    return ("True: " + word + " is a palindrome word")
  
# testing the function is_palindrome

word = input ("Please type a palindrome word:")
print( is_palindrome(word))
  
    