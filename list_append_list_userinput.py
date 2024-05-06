list = [] # creating an empty list

user_input = input("Please type a name: \n")
list.append(user_input)
user_input1 = input("Please type a color: \n")
list.append(user_input1)
if user_input1 in user_input:
  print(user_input + "is in the list")
print("Your list has", len(list), "elements: ", list)