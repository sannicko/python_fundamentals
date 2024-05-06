
# This function takes an input list and a window size named win. It calculates the total number of windows that can be formed from the list and iterates over each window, finding the maximum value within each window and storing it in a list. The function finds the maximum value for each contiguous sublist of size win in the input list.

def find_maximums(list, win):
    max_values = []
    total_windows = len(list) - win + 1
    for i in range(total_windows):
        window = list[i : i + win]
        max_val = max(window)
        print(f"Window #{i + 1}: {window}, max = {max_val}")
        max_values.append(max_val)
    return total_windows, max_values

# calling the function example use case

list1 = [1, 2, 3, 1, 4, 5]
win = 3
total_windows, result = find_maximums(list1, win)
print("The list is =", list1)
print("Total windows on array:", total_windows)
print("Output:", result)
