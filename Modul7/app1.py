class Product:

    def __init__(self):
        self.category = input("Introduceti numele categoriei: ")
        self.name = input("Introduceti numele produsului: ")
        self.price = input("Introduceti pretul produsului: ")
        self.stock = input("Introduceti stocul produsului: ")

    def __repr__(self):
        return 16 * "=" + "\n" + f"Categoria: {self.category}" + "\n" + 16 * "=" + "\n" + f"Nume: {self.name}" + "\n" + f"Pret: {self.price}" + "\n" + f"Stoc: {self.stock}" + "\n" + 16 * "-"

if __name__ == "__main__":
    camasi = Product()
    print(camasi)