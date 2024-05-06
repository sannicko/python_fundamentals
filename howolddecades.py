from datetime import datetime

name = input("What's your name: \n")
birth_date = int(input("Type your birth year: \n"))
current_date = datetime.today().year
age = current_date - birth_date
decades = age // 10 
years = age % 10
print (name, "You are", decades, "decades, and", years, "years old.")