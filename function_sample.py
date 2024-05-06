def hello(name):
  print("Hello", name)
  
# Main 

input_name = input("Enter your name: \n")

hello(input_name)

def sum(a, b):
  return a + b

def main():
  num1 = int(input("Enter a number: \n"))
  num2 = int(input("Enter another number: \n"))

  # calling the function
  result = sum(num1, num2)
  print ("The result is", result)
main()

