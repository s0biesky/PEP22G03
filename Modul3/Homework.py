# 1
# list = ["abc", 123, "1", 1]
# for i in list:
#     print(i ,type(i).__name__)

# 2
vocale = ["a", "e", "i", "o", "u"]
str = input("Introduceti un cuvant: ").lower()
list = []
list[:0] = str
a = list.count("a")
e = list.count("e")
i = list.count("i")
o = list.count("o")
u = list.count("u")
x = list.count("ă")
y = list.count("â")
z = list.count("î")
# print("Vocale in cuvantul ", str, ": ", (a + e + i + o + u + x + y + z), sep="")
print("Sunt ", (a + e + i + o + u + x + y + z), " vocale in cuvantul ", str, ".", sep="")