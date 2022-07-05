# Tuples

# my_tuple = ("a", 1, None, "a")
# print(type(my_tuple))

# Tuple Methods

# result = my_tuple.count("a")
# print(f"Numarul de obiecte in tuple: {result}")
# print(len(my_tuple))

# Tuple Slice

# result = my_tuple[1:3]
# print("Slice:", result)

# Unpacking tuple

# var1, var2, var3, var4 = my_tuple
# print(var1, var2, var3, var4)

# Packing tuple

# var1, *var2, var3 = my_tuple    # * - inglobeaza ce ramane din tuple si baga intr-o singura variabila
# print(var1, var2, var3)

# Args as tuple

# def my_print(*args):
#     print(type(args))
#     print(args)
# my_print("Value 1", "Value 2", "123")   # dynamic number of arguments (de la *)

# def my_print(args, *args2):
#     print(type(args))
#     print(args)
#
#     print(type(args2))
#     print(args2)
# my_print("Value 1", "Value 2", "123")   # dynamic number of arguments (de la *)

# Dictionare

# my_dict = {"key1": None, 123: "abcd", True: (1, 2, 3)}
# print(my_dict)
# print(type(my_dict))

# Metode

# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)
#
# print(my_dict.values())
# for value in my_dict.values():
#     print(value)
#
# print(my_dict.items())
# for item in my_dict.values():
#     print(item)

# for key, value in my_dict.items():
#     print(key, value)

# Understanding dict items

# result = my_dict.items()
# itered = result.__iter__()
# key, value = next(itered)
# print(next(itered))
# print(next(itered))
# print(next(itered))
# print(key, value)
# key, value = next(itered)
# print(key, value)
# key, value = next(itered)
# print(key, value)

