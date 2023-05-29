# the function expand_string() takes a list of strings, concatenates them, and returns the resulting string that is repeated three times and uppercase.


# define function expand_string
def expand_string(str_expand):
  # concatenate the elements of the list into a single string separated by a space
  conca_str_expand = ' '.join(str_expand)
  return (conca_str_expand * 3).upper()  # multiply the concatenated string by 3 and convert it to uppercase and return the expanded and uppercase string

print(expand_string (['This', 'is', 'the', 'test', 'expanding', 'a', 'string'])) # call and test the function expand_string