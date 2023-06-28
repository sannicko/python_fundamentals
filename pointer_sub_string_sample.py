# this function uses a sliding window technique to search for a substring within a larger string. This approach improves efficiency by avoiding redundant comparisons. It shifts the windows by one position at a time, eliminating the need to recompare the entire window for each shift.


def find_substring(string, substring):
  pointer1 = 0
  pointer2 = len(substring)
  
  while pointer2 <= len(string):
    if string[pointer1:pointer2] == substring:
      print("Found substring at index", pointer1)
      return substring 
    pointer1 += 1
    pointer2 += 1
  return False
   
string1 = "abcdefg"
substring1 = "de"

result = find_substring(string1, substring1)
print (result)

  
    