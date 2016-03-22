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


# print(randomPrime())
def gcd(a, b):
    """Compute GCD of two numbers"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(36, 6))


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


# print(multiplicative_inverse(94, 15))


def generateRSAKeys(p, q):
    """Generate RSA Public and Private Keys from prime numbers p & q"""

    n = p * q
    m = (p - 1) * (q - 1)

    # Generate a number e so that gcd(n, e) = 1, start with e = 3
    e = 3

    while 1:
        if gcd(m, e) == 1:
            break
        else:
            e += 2

    # start with a number d = m/e will be at least 1

    d = multiplicative_inverse(m, e)

    # Return a tuple of public and private keys
    return (n, e), (n, d)

#implement rsa algorithm to encrypt/decrypt
def rsa(m, in_put, n):
    return_data = 1
    m = m % n

    while in_put != 0:
        if in_put % 2 == 1:
            return_data = (return_data * m) % n
        m = (m * m) % n
        in_put /= 2

    return return_data


# +++++++++++++++++Encryption Function+++++++++++++++++
def encrypt():
    a = randomPrime()
    b = randomPrime()
    # print(a)

    print("Generating keys .......")
    (publickey, privatekey) = generateRSAKeys(a, b)

    print("Public Key (n, e) =", publickey)
    print("Private Key (n, d) =", privatekey)

    n, e = publickey
    n, d = privatekey

    # get plaintext the user input
    plaintext = entryvalue.get()

    plaintext1 = int(plaintext)
    encryptedText = rsa(plaintext1, d, n)

    listbox.insert(0, encryptedText)

    return n, d



root = Tk()
# GUI title
root.title('RSA')

# ******************plaintext input*****************
l = Label(root, text='Input the plaintext')
l.pack()

# input plaintext
entryvalue = Entry(root)
entryvalue.pack()

# click the Encrypt button
button = Button(root, text="Encrypt", command=encrypt)
button.pack()

# show the ciphertext info.
show = Label(root, text='Show Ciphertext:')
show.pack()
listbox = Listbox(root, height=2, width=60)
listbox.pack()


root.mainloop()