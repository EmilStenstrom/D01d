from math import factorial

def bin(n, k):
    if n > k:
        return factorial(n) / (factorial(k)*factorial(n-k))

print bin(20001, 10000)
