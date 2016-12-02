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
