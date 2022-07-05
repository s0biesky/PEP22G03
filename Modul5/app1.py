import pachet1

inventar = {}

if __name__ == "__main__":  # verifica daca numele sau variabila name este main sau nu, daca executam un modul de python atunci automat, acea variabila se seteaza cu valoarea main, daca este importat, contine numele

    mesaj = input("""
Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire
Introduceti optiunea dvs: """)
    while mesaj != "4":

        if mesaj == "1":
            print(inventar)

        if mesaj == "2":
            pachet1.fadaugare(inventar)
            print(inventar)
        mesaj = input("""
Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire
Introduceti optiunea dvs: """)
        if mesaj == "3":
            pachet1.fstergere(inventar)
            print(inventar)