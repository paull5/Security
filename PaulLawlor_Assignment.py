"""
Security Assignment:Implement RSA algorithm with GUI
Author: Paul lawlor
1)Generate 2 large prime numbers p & q
2)Calculate n = p*q
3)Find e such that e and x = (p-1)(q-1) are relatively prime or gcd (x, e) = 1
The numbers n and e make up your public key.
4)Calculate d so that ((d * e) - 1) % m = 1(Find a number 'd' so that the product of 'd' * 'e'
subtracted by 1 is perfectly divisible by m)
this is called finding the multiplicative inverse of a number modulo 'n'
5)Encrypt message m via c = me mod n
6)Decrypt the ciphertext c via m = cd mod n

"""

import random
from tkinter import *


def randomPrime():
    """Generate 2 random prime numbers and check if they are prime"""
    prime = False
    a = random.getrandbits(128)
    """
    With a**0.5, finding the square root of a.
    you only need to go halfway the factors of the number to see if it is prime,
    and this halfway point can be found by taking the number's square root.
    """
    while not prime:
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


def multiplicative_inverse(t, e):
    """Find the multiplicative inverse of a mod b
     using extended Euclidean algorithm"""
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

        return (t + lastY)


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


def rsa(m, in_put, n):
    """Implement the RSA algorithm to encrypt/decrypt"""
    return_data = 1
    m = m % n

    # Encrypt message m via c = me mod n
    # Decrypt the ciphertext c via m = cd mod n
    while in_put != 0:
        if in_put % 2 == 1:
            return_data = (return_data * m) % n
        m = (m * m) % n
        in_put /= 2

    return return_data


# +++++++++++++++++Encryption Function+++++++++++++++++
def encrypt():
    """Generate 2 random numbers get user input to be encrypted,
    use rsa function to encrypt data coming in, return private key values"""
    a = randomPrime()
    b = randomPrime()
    # print(a)

    print("Generating keys .......")
    (privatekey, publickey) = generateRSAKeys(a, b)

    print("Public Key (n, e) =", publickey)
    print("Private Key (n, d) =", privatekey)

    n, e = publickey
    n, d = privatekey

    # get plaintext the user input
    plaintext = entryvalue.get()

    # convert the string input to integer
    plaintext1 = int(plaintext)

    # use public key to encrypt
    encryptedText = rsa(plaintext1, e, n)

    # pass the encrypted text to the gui
    listbox.insert(0, encryptedText)

    return n, d


def decrypt():
    """Take in key from encrypt function, get user input to be decrypted,
    use rsa function to decrypt data coming in"""
    a, b = encrypt()

    # print(a)

    (privatekey, publickey) = generateRSAKeys(a, b)

    n, d = privatekey
    n, e = publickey

    # get plaintext the user input
    encryptedtext = entryvalue.get()

    # convert the string input to integer
    encryptedtext1 = int(encryptedtext)

    # use private key to decrypt
    decryptedText = rsa(encryptedtext1, d, n)

    # pass the encrypted text to the gui
    listbox2.insert(0, decryptedText)


# *******************GUI Area**************************************
root = Tk()
# GUI title
root.title('RSA')

# ******************plaintext input*****************
label = Label(root, text='Input the plaintext')
label.pack()

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

# ******************ciphertext input*****************
label1 = Label(root, text='Input the ciphertext')
label1.pack()

# input ciphertext
entryvalue2 = Entry(root)
entryvalue2.pack()

# click the Decrypt button
button2 = Button(root, text="Decrypt", command=decrypt)
button2.pack()

# show the plaintext info.
show2 = Label(root, text='Show Plaintext:')
show2.pack()
listbox2 = Listbox(root, height=2, width=60)
listbox2.pack()

root.mainloop()
