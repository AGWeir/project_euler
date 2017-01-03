"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def isprime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return a
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i <= math.sqrt(n):
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
        
def largestprime(n):
    i = int(math.sqrt(n))
    while i > 0:
        if n % i == 0:
            if isprime(i):
                return i
        i -= 1
 
largestprime(600851475143)
