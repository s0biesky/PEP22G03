# Functii

# def putere_doi(x):
#     print(x * x)
# def putere_n(x, n):
#     print(x ** n)
# putere_doi(3)
# putere_n(2, 3)

# def putere_n(x, n):
#     return x ** n
# result = putere_n(2, 3)
# print(result)
# print(putere_n(3, 3))

# Argumente

# def putere_n(x, n):
#     print("Variabilele sunt:", x, n)
#     return x ** n
# putere_n(3, 4)

# def putere_n(x, n, add = 100, sub = 0):
#     print("Valoare1 argument cheie", add)
#     print("Valoare2 argument cheie", sub)
#     print("Variabilele sunt:", x, n)
#     return x ** n + add + sub
# putere_n(3, 4, add = 201)
# putere_n(3, 4, 200)
# putere_n(3, 4, 200, 150)

# Variabile

# add = 200
# sub = 100
# div = 3
# def putere_n(n, x, add = 100, sub = 0):         # add si sub definite inca o data in functie
#     print("Valoare1 argument cheie", add)
#     print("Valoare2 argument cheie", sub)
#     print("Variabilele sunt:", x, n)
#     return (x ** n + add + sub) / div
# print(putere_n(3,3))

# add = 200
# sub = 100
# div = 3     # Var globala
# def putere_n(n, x, add = 100, sub = 0):
#     global div # obliga la folosirea variabilei globale
#     print("Valoare1 argument cheie", add)
#     print("Valoare2 argument cheie", sub)
#     print("Variabilele sunt:", x, n)
#     div = 5     # Var locala
#     return (x ** n + add + sub) / div
# print(putere_n(3, 3, 25, -25))
# print("Div result:", div)

# Nested functions

# def level1(arg1):
#     print(arg1)
#     def level2(arg2):
#         print(arg2 + arg1)
#     level2(arg1)
# level1(1)

# arg1 = 2
# def level1(arg1):
#     print("inainte de modificare", arg1)
#     def level2(arg2):
#         nonlocal arg1 # nonlocal cauta variabila intr o functie "parinte" si apoi o foloseste / modifica. Se modifica la nivel de nivel.
#         arg1 = 10
#         print(arg2 + arg1)
#     level2(3)
#     print("dupa modificare", arg1)
# level1(1)
# print("variabila globala", arg1)

# def functie():                                                                                   # de refacut
#     if len(parola) < 7:
#         print("Parola trebuie sa aiba o lungime mai mare de 7 caractere.")
#     for i in parola:
#         if i.isdigit():
#             ""
#         else:
#             print("Parola trebuie sa contina o cifra.")
#             break
#         break
#     if not parola.__contains__("%"):
#         print("Parola trebuie sa contina una din urmatoarele caractere: !, @, %.")
# parola = input("Introduceti o parola: ")
# functie()

# def functie():                                                               # de refacut
#     if len(parola) < 7:
#         print("Parola trebuie sa aiba o lungime mai mare de 7 caractere.")
#     lista = [i for i in parola if i.isdigit()]
#     if lista == True:
#         print("Parola trebuie sa contina o cifra.")
#
# parola = input("Introduceti o parola: ")
# functie()

#call method
def test():
    print("Dummy")
test()
test.__call__()