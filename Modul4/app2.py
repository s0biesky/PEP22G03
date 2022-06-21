numar = input("Introduceti un numar: ")
def functie(numar):
    while True:
        putere = input("Introduceti puterea: ")
        if putere.lower() == "Q".lower():
            print("Stop")
            break
        else:
            print("Rezultatul este:",int(numar) ** int(putere))
functie(numar)