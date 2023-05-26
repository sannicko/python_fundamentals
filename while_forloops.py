# approach #1: using while loops
def sum1_to_10_while():
  sum = 0
  num = 1

  while num <= 10:
    sum += num
    num += 1
    
  return sum


# approach #2: using for loops
def sum1_to_10_for():
  sum = 0

  for num in range(1,11):
    sum += num

  return sum

# calling the functions

result_while = sum1_to_10_while()
print("Sum using while loop:", result_while)

result_for = sum1_to_10_for()
print("Sum using for loop:", result_for)