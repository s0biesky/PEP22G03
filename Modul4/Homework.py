# 1

# def functie():
#     for x in range(10,21):
#         y = 3 * x
#         print(f"============= X = {x} =============\n Rezultatul functiei: {3 * x ** 2 - 4 * y + 4}")
#
# functie()

# 2

# nr = input("Cate carti doriti sa adaugat in bilbioteca? ")
# lista_carti = []
# for i in range(int(nr)):
#     print(f"======== Cartea {i+1} ========")
#     nume = input("Introduceti numele cartii: ")
#     autor = input("Introduceti numele autorului: ")
#     an = input("Introduceti anul publicarii: ")
#     dictionar = {"Nume: ": nume, "Autor: ": autor, "An: ": an}
#     lista_carti.append(dictionar)
#
# print("Cartile dumneavoastra sunt: ", lista_carti)

# 3

nr = input("Cate carti doriti sa adaugat in bilbioteca? ")
lista_carti = []
for i in range(int(nr)):
    print(f"======== Cartea {i+1} ========")
    nume = input("Introduceti numele cartii: ")
    autor = input("Introduceti numele autorului: ")
    an = input("Introduceti anul publicarii: ")
    dictionar = {"Nume: ": nume, "Autor: ": autor, "An: ": an}
    lista_carti.append(dictionar)
print("Cartile dumneavoastra sunt: ", lista_carti)
anul = input("Anul: ")
for i in lista_carti:
    if int(i["An: "]) > int(anul):
        print(i["Nume: "], f"a fost publicata dupa {i['An: ']}.")