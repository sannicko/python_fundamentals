
# The function called diagonal_sum that calculates the sum of the elements along the left diagonal of a square matrix m. This function calculates the sum of the elements along the left diagonal of a given square matrix and demonstrates its functionality with the provided on matrix m.

def diagonal_sum(m):
  n = len(m)
  total = 0
  for i in range(n):
    total += m[i][i]
  return total

# matrix m
m = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]] 

print("Input: ", m)
print("Output: ", diagonal_sum(m)) 

m = [[1]]
print("\nInput: ", m)
print("Output: ", diagonal_sum(m)) 