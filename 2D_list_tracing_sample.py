

# sample # 1

# The function tracing_average calculate the sum of the elements in the list and the count of the elements, respectively. After iterating through all the elements, the function computes the average by dividing the sum (y) by the count (c). The result (average) is returned as the output of the function.

def tracing_average(x):
  y = 0
  c = 0
  for i in x:
    for j in i:
      y += j
      c += 1
  return y / c

result = tracing_average([[1, 2, 3], [1, 2, 3]])
print(result)


# sample # 2

# The function tracing_max_value starts with y set to 1 (the first element of the list). It then compares each element in the list with the current value of y and updates y to be the maximum value encountered using nested loops. After iterating through all the elements, the function returns the value of y, which would be the maximum value found in the 2D list.

def tracing_max_value(x):
  y = x[0][0]

  for i in x:
    for j in i:
      if j > y:
        y = j
  return y

result = tracing_max_value([[1, 3], [5, 5], [23]])
print(result)


# sample # 3

# The function iterates over each element i in the list x. It checks if the length of i is less than the current value of y. If it is, then y is updated with the length of i. Essentially, the function finds the length of the smallest sub-list in the given 2D list.

def smallest_sublist(x):
  y = len(x[0])
  for i in x:
    if len(i) < y:
        y = len(i)
  return y

result = smallest_sublist([[1,3], [5,51,33,13], [22]])
print(result)

# sample # 4

# The function then iterates over the rows and columns of the 2D list using nested for loops. It starts from the last row and last column and prints the corresponding element using print(lst[-row][-col], end=" "). The end=" " argument ensures that the elements are printed with a space separator instead of a newline.

def mystery(lst):
  output = ""
  for row in range(1, len(lst) + 1):
   for col in range(1, len(lst[0]) + 1):
      print(lst[-row][-col], end =" ")
  return output
      
result = mystery([[1,2,3], [4,5,6]])
print(result)