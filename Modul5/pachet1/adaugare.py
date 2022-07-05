def fadaugare(inventar):
    produs = input("Introduceti produsul, pretul si stocul: ").split(",")
    inventar.update({produs[0].strip(): (produs[1], produs[2])})