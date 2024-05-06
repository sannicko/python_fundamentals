
money_owned = float(input("How much do you owe?\n"))
interest = float(input("What's the interest rate?\n"))
payment = float(input("How much is the montly payment?\n"))
months = int(input("How many months do you want to calculate?\n"))

montly_rate = interest/100/12

for i in range(months):

  interest_paid = money_owned*montly_rate
  money_owned += interest_paid - payment
  
  if (money_owned - payment < 0):
    print('The last payment is', money_owned)
    print('You paid off the loan in', i+1, 'months')
    break
  
  rounded_value_interest_paid = round(interest_paid, 3) # to round the total 3 decimal places

  rounded_value_money_owned = round(money_owned, 3) # to round the total 3 decimal places

  print( 'Month', i + 1, 'Paid', payment, 'it was', rounded_value_interest_paid, 'interest', end=' ')
  print('The balance is', rounded_value_money_owned)