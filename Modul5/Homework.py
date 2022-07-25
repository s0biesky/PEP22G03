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

