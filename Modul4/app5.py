def suma(lista: list):
    result = sum(lista)
    print(result)

def medie(list):
    #return = suma(list) / len(list)
    pass

def putere(list):
    pass

meniu = {
    "1": medie,
    "2": suma,
    "3": putere
}

# a)
list = []
print("Introduceti numere. Cand sunteti gata, introduceti x.")
while True:
    numar = input("Numar: ")
    if numar.lower() == "X".lower():
        print("Stop")
        break
    else:
        numar = float(numar)
        list.append(numar)
# b)
mesaj = input("""Meniu:
1. Media numerelor
2. Suma numerelor
3. Puterea numerelor din lista de numere
4. Iesire
Introduceti optiunea dvs: """)

my_function = meniu[mesaj]