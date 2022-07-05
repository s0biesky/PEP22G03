# Functii
# def mesaj():
#     print("Va rog sa introduceti o valoare: ")
# mesaj()
# a = int(input())
# mesaj()
# b = int(input())
# mesaj()
# c = int(input())

# def message(number):
#     print("Enter a number:", number)
# message(1)

# def message(number):
#     print("Enter a number:", number)
#
# number = 1234
# message(number)

# def message(what, number):
#     print("Enter", what, "number", number)
#
# message("pret shaorma", 15)

# def my_function(a, b, c):
#     print(a, b, c)
# my_function(1, 2, 3)

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction("Topală", "Raul")
# introduction("Bogdanov", "Ivan")

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction("Skywalker", "Luke")
# introduction("Quick", "Jesse")
# introduction("Kent", "Clark")

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction(first_name = "Raul", last_name = "Topală")
# introduction(last_name = "Topală", first_name = "Raul")

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)
#
# adding(1, 2, 3) # argument pozitional
# adding(c = 3, a = 2, b = 1) # argument keyword
# adding(3, c = 2, b = 1) # mix intre pozitional si keyword
# adding(3, 1, c = 2) # mix intre pozitional si keyword

# def introduction(first_name="John", last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)
#
# introduction()

# def introduction(first_name="John", last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)
#
# introduction(last_name="Hopkins")

# def hi(name):
#     print("Hi,", name)
#
# hi("Greg")

# def hi_all(name_1, name_2):
#     print("Hi,", name_2)
#     print("Hi,", name_1)
#
# hi_all("Sebastian", "Konrad")

# def address(street, city, postal_code):
#     print("Your address is:", street, "St.,", city, postal_code)
#
# s = input("Street: ")
# p_c = input("Postal Code: ")
# c = input("City: ")
#
# address(s, c, p_c)

# def add_numbers(a, c, b = 2): # argumentele pozitionale trebuie sa fie declarate inaintea argumentelor keyword !
#     print(a + b + c)
#
# add_numbers(a = 1, c = 3)

# Return (fara expresie) - atunci cand se afla intr-o functie, Return opreste functia si codul se intoarce la locul invocatiei

# def happy_new_year(wishes=True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy New Year!")
#
# happy_new_year(False)

# Return <expresie> (cu expresie) - 1. Termina functia 2. evalueaza si returneaza valoarea expresiei

# def boring_function():
#     return 123
#
# x = boring_function()
# print("The boring_function has returned its result. It's:", x)

# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123
#
# print("This lesson is interesting!")
# boring_function()                          # aici se pierde valoarea expresiei
# print("This lesson is boring...")

# None - cand o functie nu returneaza nimic, returneaza "None".
# None poate fi folosit pentru a compara continutul variabilelor, se poate atribui unei variabile

# def boring_function():
#     print("'Boredom Mode' ON.")
#     return
#
# print("This lesson is interesting!")
# x = boring_function()
# print(x)

# value = None
# if value is None:
#     print("Sorry, you don't carry any value")

# def strange_function(n):
#     if(n % 2 == 0):
#         return True
#     # else: return False
#
# print(strange_function(2))
# print(strange_function(1))


