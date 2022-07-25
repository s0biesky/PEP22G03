# 1

import datetime
import random

bon_string = False

def varsta(an_curent, an_cnp):
    if int(CNP[0]) > 2:
        an_nastere = 2000 + int(an_cnp)
    else:
        an_nastere = 1900 + int(an_cnp)
    if int(an_curent) - int(an_nastere) < 18:
        minor = True
        return minor

CNP = input("Introduceti CNP-ul: ")
if len(CNP) != 13:
    print("CNP-ul nu este valid.")
else:
    an_curent = int(datetime.date.today().year)
    an_cnp = CNP[1:3]
    varsta(an_curent, an_cnp)
    if varsta(an_curent, an_cnp) == True:
        print("Sunteti minor, nu puteti participa.")
    else:
        try:
            bon = float(input("Introduceti valoarea bonului: "))
        except ValueError:
            bon_string = True
        if bon_string != True:
            if bon < 100:
                lista = ["un suc", "o punga de chipsuri", "o caserola de prajituri"]
                print("Ati castigat:", random.choice(lista))
            if bon >= 100 and bon <= 500:
                lista = ["un prajitor de paine", "o consola de gaming", "o tastatura numerica"]
                print("Ati castigat:", random.choice(lista))
            if bon > 500:
                lista = ["un robot de bucatarie", "o masina", "un prajitor de paine", "o consola de gaming", "o tastatura numerica", "un suc", "o punga de chipsuri", "o caserola de prajituri"]
                print("Ati castigat:", random.choice(lista))
            print("Felicitari!!!!")
            print("-" * 35)
        else:
            print("Nu ati introdus o valoare corecta.")



# 2

lst = []
while True:
    try:
        numar = input("Introduceti un numar (cand v-ati saturat, apasati q): ")
        if numar == 'q':
            break
        numar = int(numar)
        lst.append(numar)
    except ValueError:
        continue

# Suma numarului de pe pozitia 1 si 2.
try:
    print("O sa adaugam numarul 2 si 3.")
    print("lst[1] + lst[2] = ", lst[1] + lst[2])
except IndexError:
    pass

# Divizia primelor 2 numere din lista
try:
    print("Divizia primelor 2 numere din lista este: ")
    print("lst[0] / lst[1] = ", lst[0] / lst[1])
except IndexError:
    pass
except ZeroDivisionError:
    pass
# Suma tuturor numerelor din lista
sum = 0
for i in lst:
    sum += i
print("Suma tuturor numerelor din lista este: ", sum)

# Eu asta am inteles ca trebuie facut ¯\_(ツ)_/¯