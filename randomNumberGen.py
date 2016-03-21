import random

def RandomPrime():
    prime = False
    a = random.getrandbits(128)
    b = random.getrandbits(128)



    if a % 2 != 0 :
        for x in range(3, int(a**0.5), 2):
            if a % x == 0 :
                break
            else:
                prime = True
        if b % 2 != 0 :
            for x in range(3, int(b**0.5), 2):
                if b % x == 0 :
                    break
                else:
                    prime = True

    return a, b


print(RandomPrime())