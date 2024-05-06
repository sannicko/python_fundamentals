def remainder_division(a, b):
  if b == 0:
    #raise ZeroDivisionError
    raise Exception('Divisor cannot be 0') # creating a costum exception by calling Exception constructor and passing the message as a string
  result = a//b
  remainder = a%b
  print(a, '/', b,'is', result, 'remainder', remainder)
  
# Main program calling function remainder_division

remainder_division(10, 0)