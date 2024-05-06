total = 0
paid_tips = []

num_tips = int(input("Enter # of tips this week:"))
for i in range(num_tips):
  paid_tips.append(float(input("Enter tip {} value: ".format(i+1))))

for x in paid_tips:
  total = total + x

rounded_sum = round(total, 3) # to round the total 3 decimal places

output_string = "The total of your weekly tips is: $" + str(rounded_sum).strip()

print (output_string)
