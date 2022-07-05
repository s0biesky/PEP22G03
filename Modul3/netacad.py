planta = input("Introduceti o planta: ")

if planta.lower() == "Spathiphyllum".lower():
    if planta[0].isupper():
        print("Yes - Spathiphyllum is the best plant ever!")
    else:
        print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum!"," Not ", planta, "!", sep="")