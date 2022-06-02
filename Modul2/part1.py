# #int
# number = 3
# print(type(number))
#
# number = int('3')
# print('Nr as text', type(number))
#
# #float
# number = 3.1
# print(type(number))
#
# number = float('3.1')
# print('Nr as text', type(number))

# print("Arie")
# b=10
# h=20
# arie = (b*h)/2
# print(type(arie))
# print("Arie triunghi:",arie)

# baza = input('Introduceti valoarea bazei')
# inaltime = input('Introduceti valoarea inaltimii')
# arie = (int(baza)*int(inaltime)/2)
# print(type(arie))
# print("Aria este:",arie)

# parola = 7710
# parola1 = input("Introduceti parola ")
# print(parola==int(parola1))

# nr1 = int(input("Introduceti primul numar"))
# nr2 = int(input("introduceti al doilea numar"))
# medie = (nr1+nr2)/2
# impartire = nr1//nr2
# putere = nr1**nr2
# print('Media numerelor este:',medie,'Impartirea numerelor este:',impartire,'Ridicarea la putere a numerelor este:',putere)

# venit = int(input("Introduceti venitul"))
# necesitati = (50/100)*venit
# recreativ = (30/100)*venit
# datorii = (20/100)*venit
# print("Cheltuieli uzuale:",necesitati)
# print("Recreere:",recreativ)
# print("Datorii si Economii:",datorii)

# my_number = 8**(1/2)
# print(my_number)

# a = 3
# b = 4
# c = 5
# x = (-b+((b**2-4*a*c)**(1/2)))/(2*a)
# print(x)

print("True and False is:", True and False)
print("True or False is:", True or False)
print("1 or False is:", 1 or False)
print("False or 1 is:", True or 1)
print('a or 1 is:', 'a' or 1)
print(bool('a'))
print(bool(0), bool(0.0), bool(0+0j), bool(False),bool(""))
print(bool(" "), bool(True), bool(-100), bool(0.1),bool(0+2j))
print("True xor False is:", True.__xor__(False))
print(not(True and True))