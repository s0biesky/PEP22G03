from primePy import primes
import random

def functie(x, y):
    if primes.check(x) == True and primes.check(y) == True:
        if x < y:
             z = random.randint(2, y)
             return (x ^ z) % y
        else:
            print("X trebuie sa fie mai mic decat Y.")
    else:
        print("Nu ati introdus numere prime")

x = int(input("Introduceti X: "))
y = int(input("Introduceti Y: "))
print(functie(x,y))

