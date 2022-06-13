# my_text = "My Python3 Course"
#           #0123456789
#
# #Slice with single value
# print(my_text)
# print(my_text[9])
#
# #Slice with start and stop value
# print(my_text[3:9])
# print("No start value: ",my_text[:9])
# print("No start value: ",my_text[3:])
# print("No start value: ",my_text[3:16])
#
# #Slice with start stop and step value
# print(my_text[3:9:1])
# print(my_text[3:9:2])
#
# print("No start value: ",my_text[:9:2])
# print("No stop value: ",my_text[3::2])

# text = input("Introduceti un cuvant: ")
# print(text==text[::-1])

# text = "Hello Python"
# print(text[:5],"_",text[6:], sep="")

# text = "Hello Python"
# print(text[:5]*4,"_",text[6:], sep="", end=".")

# a = 5.
# b = 5
# c = "ana"
#
# print(hex(id(a)),type(a))
# print(hex(id(b)),type(b))
# print(hex(id(c)),type(c))

# import datetime
# an = 2022
# nume = input("Introduceti numele: ")
# varsta = input("Introduceti varsta: ")
# print(f"Cum te numesti? {nume}")
# print(f"Cati ani ai? {varsta}")
# # print("Deci te-ai nascut in:",an-int(varsta))
# print("Deci te-ai nascut in:", int(datetime.date.today().year) - int(varsta))

# print("Astazi ma duc la \"facultate\"")
# print("/*\/*\*/*\/*\\", "Python", "\./\./\./\./", sep="\n")
# print("P\ty\tt\th\to\tn")

# Replace
var1 = "apa"
var2 = var1.replace("apa","suc")
print(var1,var2)

var1 = "insert insert insert"
var1 = var1.replace("ins","_",2)
print("Replaced i: ",var1)

#Pentru a vedea metodele disponibile
# print(dir(1))


