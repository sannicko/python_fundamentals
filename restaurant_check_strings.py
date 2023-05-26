# this program prompts a user for the restaurant bill amount and number of people in the party. The program calculates and prints the total amount that each person has to pay for restaurant bill in a user-friendly format.


total_bill = input("Please enter the total check: $")

total_people = input("Please enter the number of people: ")

def splitBill(total_bill, total_people):
  splitBill = float(total_bill) / int(total_people)
  return (splitBill)

split_total = splitBill(total_bill, total_people)
print("Each people has to pay:$", split_total)
    

