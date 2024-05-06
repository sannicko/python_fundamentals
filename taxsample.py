amount = int(input("What's the amount: \n"))
tax = int(input("Enter the tax percentage: \n"))
total = amount + (amount * (tax / 100))
print(total)
