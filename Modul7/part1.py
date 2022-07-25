# Objects

# class Keyboard:
#     typed = ""
#     shift_pressed = False
#
#     def press_shift(self):
#         self.shift_pressed = True
#
#     def release_shift(self):
#         self.shift_pressed = False
#
#     def press_a(self):
#         if self.shift_pressed:
#             self.typed += "A"
#         else:
#             self.typed += "a"   # <- learn self
#
#     def how_is_self(self):
#         print(id(self))
#
#
# keyboard = Keyboard()
#
# print(type(keyboard))
# print(f"valoarea este: {keyboard.typed}")
# keyboard.press_a()
# print(f"noua valoarea este: {keyboard.typed}")
# keyboard.press_a()
# print(f"noua noua valoarea este: {keyboard.typed}")
# keyboard.how_is_self()
# print(id(keyboard))
#
# # new keyboard
# keyboard1 = Keyboard()
# print(f"new keyboard - valoarea este: {keyboard1.typed}")
# keyboard1.press_shift()
# keyboard1.press_a()
# keyboard1.release_shift()
# print(f"new keyboard - noua valoarea este: {keyboard1.typed}")

# class Caine:
#     latrat = "hamhamham"
#     nervos = "mrrrr"
#     blana = ""
#     vizitator = False
#     mangaiat = False
#
#     def culoare_blana(self):
#         self.blana = "neagra"
#
#     def vizitator_avem(self):
#         self.vizitator = True
#
#     def mangaiat_da(self):
#         self.mangaiat = True
#
#     def comportament(self):
#         if self.vizitator:
#             return(self.latrat)
#         else:
#             return("silent mode ON")
#
#     def comportament2(self):
#         if self.mangaiat:
#             return(self.nervos)
#         else:
#             return("cuminte")
#
# caine = Caine()
#
# caine.culoare_blana()
# print(f"Blana cainelui este: {caine.blana}")
#
# caine.vizitator_avem()
# print(f"Caine: {caine.comportament()}")
# caine.mangaiat_da()
# print(f"Caine: {caine.comportament2()}")