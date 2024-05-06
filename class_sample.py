
class robot_cat:
  
  # the __init__() method to initialize robot's properties. self is always the first parameter in the init method, it refers to the current object. The other parameters are the values for the properties you want to initialized. This pass in the propeerties you want to initialize as parameters
    def __init__(self, name_val, breed_val):
      # then initialize the properties of the new object, self
      self.name = name_val # passed in values
      self.breed = breed_val # passed in values
    # create a class method, a method is a function that belongs to a class
    def meow(self): # self as a first parameter
      print("Meow Meow")
      
      
# create the object
# main

my_cat = robot_cat("red", "street")
print("The name is:", my_cat.name)
print("The breeed is:", my_cat.breed)
my_cat.meow() # calling the class method

      
      
       
    