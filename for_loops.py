# for Loop Syntax
# for var_name in sequence:
#   #line of code to repeat
#   doSomething
# for: keyword to identify type of loop
# var_name: placeholder for a variable name. This variable will hold each item in the sequence and change value with each iteration.
# in: This keyword is used to iterate through each item in the sequence
# sequence: A list or sequence of objects. In most cases we use the range function to create a sequence of numbers that we iterate through.
# doSomething: This is a placeholder for the code block inside the loop.

# for loop sum of numbers 1 to 10 inclusively

def sum1_to_10_for():
  sum = 0
  for num in range (1,11):
    sum += num
    print (num)
  return sum
  
print(sum1_to_10_for())