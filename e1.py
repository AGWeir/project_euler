""" 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
def euler1(n):
    s = 0
    for i in range(n):
        if (mult3(i) or mult5(i)):
            s += i
    return s
    
def mult5(n):
    return True if n % 5 == 0 else False

def mult3(n):
    return True if n % 3 == 0 else False

#This is better because if it's a multiple of 3 it doesn't need to evaluate mult5
def euler1better(n):
    s = 0
    for i in range(n):
        if i % 3 == 0:
            s += i
        elif i % 5 == 0:
            s += i
    return s

#Alternative method same performance
def euler1alt(n):
    return sum([i for i in range(n) if (i % 3 == 0 or i % 5 == 0)])
