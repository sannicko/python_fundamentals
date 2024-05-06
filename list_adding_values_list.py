
paid_tips = [9.99, 15, 17.99, 5.99] # list with values

sum = 0

for i in paid_tips:  # looping the list and add values
  sum = sum + i

rounded_sum = round(sum, 3) # to round the total 3 decimal places

print("Last week you spent $", rounded_sum, " in 5 days", sep = '')