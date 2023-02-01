# Create List Syntax
# list_name = [elem1, elem2, ...]
# list_name: variable name for our List to call in our program.
# =: We use the = sign to show assignment of the variable to a value
# [ ]: The square brackets [] are used to distinguish the List data structure.
# elem1, elem2: You may choose to include elements in your list when creating it for the first time. Elements must be separated by commas and follow the proper data type syntax (i.e Strings must be represented with quotation marks around each value.)


# temperature = [90, 87, 83, 92, 85, 86, 84]

# # first element
# print(temperature[0])  # 90

# # fourth item
# print(temperature[3])  # 92

# # negative indexing
# print(temperature[-3])  # 85

# # slicing operator
# print (temperature[2:6])

# temperature = [90, 87, 83, 92, 85, 86, 84]

# # elements index 2 to index 5
# print(temperature[2:6])  # [83, 92, 85, 86]

# # elements from index 0 to index 5
# print(temperature[0:-1]) # [90, 87, 83, 92, 85, 86]

# # beginning to end
# print(temperature[:]) # [90, 87, 83, 92, 85, 86, 84]

# # elements from index 3 to end
# print(temperature[3:]) # [92, 85, 86, 84]

# # elements from index 0 to 4
# print(temperature[:5]) # [90, 87, 83, 92, 85]

# # reassign elements

# # lists are mutable, meaning the elements can be changed. To reassign assignment to a different value, use the assignment operator =

# toppings = ["sprinkles", "whipped cream", "cherry"]

# # change the 3rd element
# toppings[2] = "hot fudge"

# print(toppings) # ["sprinkles", "whipped cream", "hot fudge"]

# # change 1st and 2nd element
# toppings[0:2] = ["cookies", "gummy bears"]

# print(toppings) # ["cookies", "gummy bears", "hot fudge"]

# # List Operations
# # len()

# # len() is a built-in function that returns the length of a list. This function takes in a List and outputs the number of elements in the list.

# grocery_list = ['milk', 'eggs', 'bread']
# len(grocery_list)  # 3
# print(len(grocery_list))

# empty_list = []
# len(empty_list)  # 0
# print (len(empty_list))

# Membership Operator: in
# The in operator checks if a value is an element of a sequence.

# grocery_list = ['milk', 'eggs', 'bread']
 
# 'milk' in grocery_list  # True
# 'butter' in grocery_list  # False
# 'Milk' in grocery_list  # False

# print ('milk' in grocery_list)
# print ('butter' in grocery_list)
# print ('Milk' in grocery_list)

my_list = ['p','r','o','b','l','e','m']
print(my_list)

my_list[2:3] = []
print(my_list)

my_list = ['p', 'r', 'b', 'l', 'e', 'm']
print(my_list)

my_list[2:5] = []
print(my_list)

my_list = ['p', 'r', 'm']
print(my_list)