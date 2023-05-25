grade = input("What is your numerical grade?")  #asking for users input

grade = int(grade) #using int function to convert string type to integer, int() syntax,  int(stringValue)

if grade > 90:
	print("A")
elif grade > 80:
  print("B")	
elif grade > 70:
	print("C")
elif grade >= 65:
	print("D")
else:
  print("F")