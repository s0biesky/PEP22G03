# 1
# my_age = 18
#
# if my_age >= 18:
#     print("You are an adult")
# elif my_age >= 13:
#     print("You are a teenager")
# elif my_age >= 0:
#     print("You are a child")
# else:
#     print("Negative values are not allowed")
#
# 2 - AND WITH CONDITION
#
# a = "a"
# b = 3
# if a:
#     print(b)
# else:
#     print(a)
#
# print(a and b)

# OR WITH CONDITION
# if a:
#     print(b)
# else:
#     print(a)
#
# print(a or b)
# a = "a"
# b = "b"
# print(a and b)
# print(bool(a and b))
# an_curent = 2022
# cnp = input("Introduceti primele 7 cifre din CNP: ")
# an = cnp[1:3]
# if int(cnp[0]) > 2:
#     an_nastere = 2000 + int(an)
# else:
#     an_nastere = 1900 + int(an)
# print(an_nastere)
# if an_curent - an_nastere >= 18:
#     print("Aveti peste 18 ani.")
# else:
#     print("Nu aveti peste 18 ani.")
#
# number = int(input("Introduceti un numar: "))
# start = 0
# if start+2 <= number:
#     start+=2
#     print(start)
# if start+2 <= number:
#     start+=2
#     print(start)
# if start+2 <= number:
#     start+=2
#     print(start)
# if start+2 <= number:
#     start+=2
#     print(start)
#
# While loop
# depends_on = 1
# while depends_on <= 4:
#     depends_on += 1
#     print("Running")
#     if depends_on == 4:
#         break
#
#
# print("Done")
#
# numar = int(input("Introduceti un numar: "))
# i = 0
# while i < numar:
#     if (i % 2) == 0:
#         print(i)
#     i += 1
#
# n = 0
# while n < 10:
#     if n == 7:
#         n += 1
#         continue
#     print(n)
#     n += 1
#
# print("Done")
#
# n = 0
# while n < 10:
#     if n == 7:
#         n += 1
#         continue
#     print(n)
#     n += 1
# else:
#     print("Done")
#
# n = 0
# while n < 10:
#     if n == 7:
#         n += 1
#         break
#     print(n)
#     n += 1
# else:
#     print("Done")
#
# print("1. Cappuccino - 4 lei", "2. Espresso - 3.5 lei", sep="\n")
# cafea = input("Care sa fie? [1,2]: ")
# if str(cafea) == str(1):
#     bacnota = int(input("Introduceti o bacnota [5,10]: "))
#     if bacnota == 5:
#         print("Veti primi restul de", bacnota - 4, "lei.")
#         print("Produsul se livreaza.")
#     elif bacnota == 10:
#         print("Veti primi restul de", bacnota - 4, "lei.")
#         print("Produsul se livreaza.")
#     else:
#         print("Bacnota gresita!")
# if str(cafea) == str(2):
#     bacnota = int(input("Introduceti o bacnota [5,10]: "))
#     if bacnota == 5:
#         print("Veti primi restul de", bacnota - 3.5, "lei.")
#         print("Produsul se livreaza.")
#     elif bacnota == 10:
#         print("Veti primi restul de", bacnota - 3.5, "lei.")
#         print("Produsul se livreaza.")
#     else:
#         print("Bacnota gresita!")
#
# i = 1
# while input("Introduceti parola: ") != "7788":
#     if i == 3:
#         print("Ati introdus parola gresit de 3 ori, cardul este acum blocat.")
#         break
#     i += 1
#     print("Parola gresita. Mai incercati.")
# else:
#     print("Acces permis.")