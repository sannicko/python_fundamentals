# this is a program that functions as a ordering system. These are the functionalities:
# print a numbered list of the menu items.
# continuously ask the user for the item number they want to add to their order.
# stop prompting the user to enter item numbers if user enters done.
# print a goodbye message and the items in the order.

def food_order(): 
  menu = ["rice", "salmon", "tuna", "salad" ] # create a list with menu items
  print ("Select the numbers of the menu")
  for index, val in enumerate(menu):
      print(index+1, ":", val)
  order = [] # create an empty list to add the menu order
  items = int(input("1-10 (type 'done' to finish): "))
  menu_item = menu[items-1] # add selected items to list [order]
  order.append(menu_item)
  
  while True: # while loop to keep asking for items until the user enters "done"
    item = input("\nWould you like anything else? ").lower()
    
    if item == "done":
      break
    menu_item = menu[int(item)-1]
    order.append(menu_item)
  print ("\nThank you for your order! You ordered: ")
  for item in order: # for loop to print order
    print(item)
  
  return("******************")
 

print (food_order()) # call the function food_order