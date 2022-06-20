# hello = "Hello x Python"

# for letter in hello:
#     if "x" == letter:
#         break
#     print(letter)
# else:
#     print("x is not present")

# my_number = 123
#
# for number in my_number:
#     if 1 == number:
#         continue
#     print(number)
# else:
#     print("1 was removed from number")

# how does for work
# hello = "abc"
# iterated_object = hello.__iter__()
# print(iterated_object)
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))    # <- end of loop (StopIteration)

# exemplu care nu functioneaza
# hello = 123
# iterated_object = hello.__iter__()
# print(iterated_object)
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))    # <- end of loop (StopIteration)

# hello = range(1, 11, 2)
# print(dir(hello))
# iterated_object = hello.__iter__()
# print(iterated_object)
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))    # <- end of loop (StopIteration)

# operatii pe biti
# Object type int
# -4 in bits = 11111100
# -3 in bits = 11111101
# -2 in bits = 11111110
# -1 in bits = 11111111
# 0 in bits = 00000000
# 1 in bits = 00000001
# 2 in bits = 00000010
# 3 in bits = 00000011

# and bits
# print(1 and 2)
# print(1 & 2)    # 00000001 & 00000010 result 00000000 = 0
# or bits
# print(-2 or 2)
# print(-2 | 2)   # 11111110 | 00000010 result 11111110 = -2
# xor bits
# print(-3 ^ 3)   # 11111101 ^ 00000011 result 11111110 = -2
# print(-2 ^ 3)   # 11111110 ^ 00000011 result 11111101 = -3

# print((146 ^ 21) ^ 21)
# print(("a" ^ "b") ^ "b")
# print(ord("r"))
# print(chr(114))
# print((ord("a") ^ ord("b")) ^ ord("b"))
# print(chr(97))

# my_test = "Hello Python"
# key = "A"
# key2 = ord(key)
# encrypted_text = ""
# for letter in my_test:
#     letter_code = ord(letter)
#     encrypted_letter = letter_code ^ key2
#     encrypted_text += chr(encrypted_letter)
# print(encrypted_text)
# decrypted_text = ""
# for letter in encrypted_text:
#     letter_code = ord(letter)
#     encrypted_letter = letter_code ^ key2
#     decrypted_text += chr(encrypted_letter)
# print(decrypted_text)

# text = input("Introduceti un cuvant (fara majuscule): ")
# contor = 0
# for letter in text:
#     if letter == text[0]:
#         contor = contor + 1
# print("r apare de:", contor, "ori.")

# text=input("Introduceti un cuvant (fara majuscule): ")
# count=0
# repetare=input("Introduceti litera care sa fie numarata (fara majusucle): ")
# for i in text:
#     if i==repetare:
#         count+=1
# print(repetare, "se repeta de", count, "ori.")

# cuvant = input("Introduceti un cuvant: ").lower()
#
# print(f"{cuvant[0]} apare de {cuvant.count(cuvant[0])} ori")

# cuvant = input("Introduceti un cuvant: ").lower()
# counter = 0
# repetition = input("Introduceti caracterul: ").lower()
# for letter in cuvant:
#     if letter == repetition:
#         counter += 1
# print(f"{repetition} se repeta de {counter} ori")

# Liste
# my_var = "abc"
# my_list = ["a", 123, True, my_var]
#
# for object_ in my_list:
#     print(object_)
# print("#"*80)

# my_list = ["a", 123, True, my_var]
# my_string = "Hello Python"
# for object_ in my_string:
#     my_string += object_
# print(my_string)

# my_list = ["a", 123, True, my_var]
# my_string = "Hello Python"
# for object_ in my_list:
#     print(id(my_list))
#     my_list.append(object_) # list is mutable - do not do this
# print(my_list)
# list_copy = my_list.copy()
# print("copied ID: ", [id(list_copy)])
# for object_ in my_list.copy():
#     print(id(my_list))
#     my_list.append(object_)
# print(my_list)
# for object_ in my_string:
#     print(id(my_string))
#     my_string += object_
# print(my_string)

# my_list = ["Masa", 5, "Scaun", 4.5, [5,6,7], 8]
# for i in my_list:
#     print("Tipul obiectului", i, "este", type(i).__name__)

# lista = input("Introduceti lista de taskuri: ")
# lista_taskuri = lista.split(",")
# print(lista_taskuri)
# for task in lista_taskuri.copy():
#     lista_taskuri.count(task)
#     print(f"Task-ul {task} se regaseste de {lista_taskuri.count(task)} ori.")
#     if lista_taskuri.count(task) > 1:
#         lista_taskuri.remove(task)
# print(lista_taskuri)