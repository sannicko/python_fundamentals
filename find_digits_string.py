import random
import string

num_digits = random.randint(3, 7)  # generate a random number of digits between 3 and 7
num_letters = 15 - num_digits  # calculate the number of letters needed to complete the total length

digits = random.choices(string.digits, k=num_digits)  # generate random digits
letters = random.choices(string.ascii_letters, k=num_letters)  # generate random letters

mixed_chars = digits + letters  # combine the lists of digits and letters
random.shuffle(mixed_chars)  # shuffle the mixed characters randomly

txt = ''.join(mixed_chars)  # concatenate the mixed characters

nums = " "
count = 0
total_sum = 0

for char in txt:
    if char.isdigit():
        nums += char
        count += 1
        total_sum += int(char)

print("txt:", txt)
print("nums:", nums)
print("Sum of digits:", total_sum)
print("Average of digits:", total_sum / count)
