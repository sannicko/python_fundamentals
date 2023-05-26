import random # random library

# the syntax for the enumerate function is:

# for index, value in enumerate(list_name):
# 	# loop body
# to help index elements while iterating, the enumerate() function can be used to add a counter to each element of the list.


flavors = ["orange", "peper mint", "strawberry"]
for i, val in enumerate(flavors):
	print(i, ":", val)

def populate_sevenlist():
  sevenlist = []
  for i in range (10):
    sevenlist.append(random.randint(1,10))
  print(sevenlist)
  return sevenlist

# call the function populate_sevenlist to populate list
# sevenlist = populate_sevenlist()
# print(sevenlist)

def find_sevens(nums):
  found_sevens = False # flag to track if seven are found
  for i,val in enumerate(nums):
    if val == 7:
      print(i)
      found_sevens = True
      
  if not found_sevens:
    print("no sevens found in the list.")
    
nums = populate_sevenlist()
print ("the number seven is on index:",end = '') 
find_sevens(nums)





