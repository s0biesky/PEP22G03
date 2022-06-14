print(False or (False and True) or True)
#
# Exercițiul 1
#
parola = "Passme1n"
parolaInput = input("Introduceti parola: ")
print(parola == parolaInput)
#
# Exercițiul 2
#
# a)
nume1 = input("Introduceti primul nume: ")
nume2 = input("Introduceti al doilea nume: ")
print("Lungimea primului nume este: " + str(len(nume1)))
# b)
if nume1 == nume2:
    print("Cele doua nume sunt la fel.")
else:
    print("Cele doua nume nu sunt la fel.")
# c)
if len(nume1) > len(nume2):
    print("Primul nume este mai lung decat cel de-al doilea nume.")
else:
    print("Primul nume nu este mai lung decat cel de-al doilea nume.")
# d)
print("Initiala primului nume este:", nume1[0])
# e)
print("Inversul primului nume este:", nume1[::-1])
#
# Exercițiul 3
#
# a)
nume1 = input("Introduceti primul nume: ")
nume2 = input("Introduceti al doilea nume: ")
print("Lungimea primului nume este: " + str(len(nume1)))
# b)
if nume1 == nume2:
    print("Cele doua nume sunt la fel.")
else:
    print("Cele doua nume nu sunt la fel.")
# c)
if len(nume1) > len(nume2):
    print("Primul nume este mai lung decat cel de-al doilea nume.")
else:
    print("Primul nume nu este mai lung decat cel de-al doilea nume.")
# d)
print("Initiala primului nume este:", nume1[0])
# e)
print("Inversul primului nume este:", nume1[::-1])
# f)
numar = int(input("Introduceti un numar: "))
print(nume1*numar)
#
# Exercițiul 4
#
# a)
variabila = "Ananas"
i = 0
while i < len(variabila):
    print(variabila[i])
    i += 1
# b)
print(variabila[0:3], variabila[3:6], sep="\n")
# c)
print(variabila[0:2], variabila[2:5], variabila[5], sep=":")
# d)
print(variabila[0:3], variabila[3:5], variabila[5], sep="_")
# e)
print(variabila[1:5]*4)

# Suplimentar
# 1)
cuvant = input("Introduceti un cuvant: ")
print(cuvant.lower() == cuvant.lower()[::-1])
# 2)
sir = input("Introduceti un sir: ")
print("Sirul incepe cu o majuscula:", sir[0].isupper())
