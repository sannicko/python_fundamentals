# this function checks if a given list has three consecutive elements with a value of 555, if yes returns True. Otherwise, it returns False.

# keep in mind lists are mutable, which means you can modify their elements. You can perform various operations on lists, such as adding or removing elements, sorting, and iterating over the elements using loops.

def has_555(numbers):   
    for i in range(len(numbers) - 2):
        if numbers[i] == 5 and numbers[i+1] == 5 and numbers[i+2] == 5:
            return True
    return False

# call the function
numbers = [1, 3, 4, 5, 5, 5, 3, 5] # list numbers
result = has_555(numbers)
print("Input :", numbers)
print("Output :", result)

numbers = [1, 3, 5, 5]
result = has_555(numbers)
print("Input :", numbers)
print("Output :", result)

numbers = [5, 5, 5]
result = has_555(numbers)
print("Input :", numbers)
print("Output :", result)