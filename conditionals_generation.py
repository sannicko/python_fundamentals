import datetime


def generation(year): # define the function
  year = int(year)  # convert the input to integer
  
  if year > 2011: # determine the generation based on the year using conditional
    return ("You are generation Alpha")
  elif year > 1997 and year < 2011:
    return ("You are generation Z")
  elif year > 1981 and year < 1996:
    return ("You are generation Millennials")
  elif year > 1965 and year <= 1980:
    return ("You are generation X")
  else:
    return ("You are not from this universe")
    
def calculate_age(birth_year): # define the function
  birth_year = int(birth_year) # convert the input to integer
  current_year = datetime.datetime.now().year # get the current date
  age = current_year - birth_year # calculate the age 
  return age

# calling the functions
    
birth_year = input ("Type your birth year: ") # prompt the user to enter the birth year
result = generation(birth_year) # call the function generation
age = calculate_age(birth_year) # call the function calculate age
print(result, "and your are:", age, "years old" ) # print generation and age

