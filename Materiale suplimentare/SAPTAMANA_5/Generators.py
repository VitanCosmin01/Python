"""
Generators

Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar
intre 1 si 49 inclusiv.
Ultima apelare va da un singur număr de 'noroc' format
din 7 cifre.

"""


import random


def generator():
    total = 0
    while total < 6:
        yield random.randint(1, 49)
        total += 1


def noroc_generator():
    yield random.randint(10, 60)


lottery_num = tuple(generator())
noroc_num = tuple(noroc_generator())
print("loteria 6/49")
print(lottery_num)

print("noroc num")
print(noroc_num)

