def max_prime_factor(x):
    print "Looking for factors of", x
    factors = []
    i = 2
    while i <= x:
        if (x % i == 0):
            x = x / i
            factors.append(i)
            print "Factor", i
            i = 1
        i += 1

    print "Factors are", factors
    return max(factors)

print max_prime_factor(21)
print max_prime_factor(63)
print max_prime_factor(1000)
import sys
print max_prime_factor(sys.maxint/1000)
