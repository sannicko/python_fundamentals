# This function will search for a pair of elements that sum up to the value of X = 50. If there is no such pair in the given list, the function will return (False, "The value does not match x"). 

def find_sum_pair(list, x):
  left = 0
  right = len(list) - 1
  
  while left < right:
    current_sum = list[left] + list[right]
    
    if current_sum == x:
      return ("True the value is = ", current_sum, (list[left], list[right]))
    
    if current_sum < x:
      left += 1
    else:
      right -= 1
      
  return False, ("The value does not match x")

# calling the function

list = [10, 20, 30, 40, 55, 60, 75, 80]
x = 50

result = find_sum_pair(list, x)
print (result)    