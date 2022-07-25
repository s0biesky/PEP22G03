# Create application that will ask the user for python input and format the input prompt as needed.
# contor = 0
# while True:
#     var1 = input(">>> ")
#     if contor == 0 and var1.__contains__(":"):
#         var2 = input("...   ")
#     else:
#         break
#     contor = contor + 1
#     while len(var2) > 0:
#         if contor > 0 and not var2.__contains__(":"):
#             var2 = input("...   ")
#         else:
#             var2 = input("...")


# contor = 0
# while contor == 0:
#     var1 = input(">>> ")
# import random


def functie():
    valoare = int(input("Introduceti limita: "))
    primes = []
    for i in range(1, valoare):
        for j in range(2, i // 2 + 2):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
import random
x = functie()
y = (random.randint(x[0],x[-1]))
z = x.pop(y)
zi = (random.randint(z[0],z[-1]))
print(y, zi)
