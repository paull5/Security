import random
from tkinter import *


def randomPrime():
    prime = False
    a = random.getrandbits(8)

    while prime == False:
        if a % 2 != 0:
            for x in range(3, int(a ** 0.5), 2):
                if a % x == 0:
                    break
                else:
                    prime = True

        return a


#print(randomPrime())


def gcd(a, b):
    """Compute GCD of two numbers"""
    if a%b == 0:
        return a
    return gcd(b, a % b)

#print(gcd(12, 4))
# find the multiplicative inverse using extended euclid
def multiplicative_inverse(t, e):
    x = 0
    y = 1
    lastX = 1
    lastY = 0
    a = t
    b = e
    while b != 0:
        quotient = (a / b)

        tmpB = b
        b = (a % b)
        a = tmpB

        tmpX = x
        x = (lastX - (quotient * x))
        lastX = tmpX

        tmpY = y
        y = (lastY - (quotient * y))
        lastY = tmpY

        return t + lastY

#print(multiplicative_inverse(94, 15))
