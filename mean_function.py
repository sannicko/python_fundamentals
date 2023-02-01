# Define a function that calculates the mean 

def mean(numbers):
    # Calculate the sum of the numbers in the list
    total = sum(numbers)
    # Divide the sum by the number of elements in the list to find the mean
    average = total / len(numbers)
    # Return the calculated mean
    return average

# Define a function that calculates the median
def median(numbers):
  n = len(numbers)
  # Sort the list of numbers
  numbers.sort()
  # Check if the number of elements in the list is odd or even
  if n % 2:
    # If odd, return the middle element
    index = int(n / 2)
    return numbers[index]
  else:
    # If even, return the average of the two middle elements
    index = int(n / 2)
    return (numbers[index - 1] + numbers[index]) / 2 

# Ask the user to input 5 numbers
numbers = []
for i in range(5):
  number = int(input("Enter a number from 1 to 100: "))
  numbers.append(number)

# Call the mean and median functions with the user-entered numbers
mean_result = mean(numbers)
median_result = median(numbers)

# Print the results
print("The mean of the numbers is:", mean_result)
print("The median of the numbers is:", median_result)
