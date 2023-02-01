# This function checks if a given list has three consecutive elements with a value of 222, if yes returns True. Otherwise, it returns False.

def has_222(numbers):   
    for i in range(len(numbers) - 2):
        if numbers[i] == 2 and numbers[i+1] == 2 and numbers[i+2] == 2:
            return True
    return False

# Call the function
numbers = [1, 3, 4, 2, 2, 2, 3, 5]
result = has_222(numbers)
print("Input :", numbers)
print("Output :", result)

numbers = [1, 3, 2, 2]
result = has_222(numbers)
print("Input :", numbers)
print("Output :", result)

numbers = [2, 2, 2]
result = has_222(numbers)
print("Input :", numbers)
print("Output :", result)