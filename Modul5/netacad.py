# Module
# import math
# print(math.sin(math.pi/2))

# import math
#
# def sin(x):
#     if 2 * x == pi:
#         return 0.9999999
#     else:
#         return None
#
# pi = 3.14
#
# print(sin(pi/2))
# print(math.sin(math.pi/2))

# from math import sin, pi
#
# print(sin(pi/2))

# from math import sin, pi
#
# print(sin(pi / 2))
#
# pi = 3.14
#
#
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
#
#
# print(sin(pi / 2))

# pi = 3.14
#
#
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
#
#
# print(sin(pi / 2))
#
# from math import sin, pi
#
# print(sin(pi / 2))

# import math as m
#
# print(m.sin(m.pi/2))

# from math import pi as PI, sin as sine
#
# print(sine(PI/2))

# import math
# print(dir(math))

# from math import pi, radians, degrees, sin, cos, tan, asin
#
# ad = 90
# ar = radians(ad)
# ad = degrees(ar)
#
# print(ar)
# print(ad)
#
# print(ad == 90.)
# print(ar == pi / 2.)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)

# from math import e, exp, log
#
# print(pow(e, 1) == exp(log(e)))
# print(pow(2, 2) == exp(2 * log(2)))
# print(log(e, e) == exp(0))

# from math import ceil, floor, trunc
#
# x = 1.4
# y = 2.6
#
# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))
# print(trunc(-x), trunc(-y))

# Random:
# import random
# print(random.randint(0,1))

# from random import choice, sample
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(choice(my_list))          # choice - alege un numar din lista
# print(sample(my_list, 5))       # sample - face o lista
# print(sample(my_list, 10))

# Detalii despre statia de lucru

# from platform import platform
#
# print(platform())
# print(platform(1))
# print(platform(0, 1))

# from platform import machine
#
# print(machine())

# from platform import processor
#
# print(processor())

# from platform import system
#
# print(system())

# from platform import version
#
# print(version())

# from platform import python_implementation, python_version_tuple
#
# print(python_implementation())
#
# for atr in python_version_tuple():
#     print(atr)

# import pygame
#
# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False


