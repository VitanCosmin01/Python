'''
Singleton
Se da următoarea clasa:


class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același obiect:
Vom folosi functia `__new__` (adevăratul constructor din Python)
Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
La orice alta apelare, vom returna obiectul deja existent

'''

class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

# varianta 1

instance = None

def __new__(cls, *args):
    if not hasattr(cls, "instance"):                            #de folosit hasattr cat mai mult
            cls.instance = super().__new__(cls, *args)
    return cls.instance

#varianta 2

instance = None

def __new__(cls, *args):
    if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls, *args)
    return cls.instance

# varianta 3
class PresidentOfRomania:
    instance = None

    def new(cls, args):
        if not hasattr(cls, "instance"):
            cls.instance = super().new(cls,args)
        return cls.instance

    def str(self):
        return "I am Romania's president"

    def say_hello(self):
        return f'Salut! {self}'


a = PresidentOfRomania()
b = PresidentOfRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Same object?? {a is b}')