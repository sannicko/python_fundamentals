import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollards_rho(N):
    x = random.randint(1, N - 1)
    y = x
    c = random.randint(1, N - 1)
    d = 1
    while d == 1:
        x = (x * x + c) % N
        y = (y * y + c) % N
        y = (y * y + c) % N
        d = gcd(abs(x - y), N)
    return d

def factorize(N, e):
    p = pollards_rho(N)
    q = N // p
    return p, q

# Example usage
#N = 956468472525192587  # Example modulus N
#e = 65537    # Example public exponent e

values = [(937329730064822657, 65537),
          ]

for N, e in values:
  p, q = factorize(N, e)
  print("p:", p)
  print("q:", q)
