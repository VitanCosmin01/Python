#
# def my_func():
#     print("Hello World!")
#
#
# my_func()  # => Hello World!
#
#
# def greatings(user):
#     print(f'Hello {user}!')
#
#
# greatings("Cosmin")   # => Hello Cosmin!
#
# temperatura = 25
# if temperatura > 30:
#     # executa acest bloc de cod daca conditia_1 este adevarata
#     print("Este foarte cald!")
# elif temperatura > 20:
#     # se executa acest bloc daca conditia_1 este falsa si conditia_2 este adevarata
#     print("Este cald!")
# else:
#     # se executa acest bloc de cod daca nici conditia_1, nici conditia_2 nu sunt adevarate
#     print("Este racoare!")
#
# # => Este cald!
# my_list = ["alb", 10, True, "verde", 5.1, "alb"]
#
# my_tuple1 = ("mere", "pere", "banane")
#
# my_dict = {"brand": "Ford",
#            "model": "Mustang"}
#
#
#
#
# # initializam o variabila de tip int/numar intreg
# cantitate = 10
# # initializam o variabila de tip float/numar zecimal
# pret = 10.45
# # definim o variabila string folosind ghilimele simple
# nume = 'Cosmin'
# # definim o variabila string folosind ghilimele duble
# prenume = "Vitan"
# print(str(prenume))
# # initializam variabile de tip boolean
# este_impar = False
# este_par = True
#
#
# # declaram o variabila t cu valoarea 10
# t = 10
# # atribuim mai multe valori pentru mai
# # multe variabile in aceeasi linie
# x, y, z = "Orange", "Banana", "Cherry"
# # atribuim aceeasi valoare pentru mai
# # multe variabile in acceasi linie
# a = b = c = "Apple"
# # case sensitive
# my_var = 5
# my_Var = 10
# # my_var != my_Var
# # variabila t se suprascrie
# t = 20
# # folosirea numelor sugestive
# zahar = 5
#
# # Concatenarea stringurilor
# nume = 'Vitan'
# prenume = 'Cosmin'
# nume_complet = nume + prenume
# print(nume_complet)
# print('Numele meu este ' + nume + prenume)
# # f'string
# varsta = 40
# # print("Varsta mea este de:" + varsta) # da eroare
# print(f"Varsta mesa este de: {varsta}")
# # Slicing
# info = 'Afara sunt 2 grade'
# # Extragem string-ul care incepe cu index-ul 0 pana la index-ul 1, inclusiv
# print(info[0:2]) # => 'Af'
# # Extragem string-ul care incepe cu index-ul 0 pana la indexul 4, inclusiv
# print(info[0:5]) # => 'Afara'
# # Daca nu specificam end_pos, se va extrage string-ul
# # pana la ultimul caracter, inclusiv
# print(info[6:])  # => 'sunt 2 grade'
# # Daca nu specificam start_pos, se va extrage string-ul
# # incepand cu primul caracter.
# print(info[:5])  # => 'Afara'
# ## Inversare string
# print(info[::-1]) # => 'edarg 2 tnus arafA'
#
# # Type casting
#
# print("Hello World")
# # => Hello World
#
# print(type("Hello World"))
# # => <class 'str'>
# print(type(10))
# # => <class 'int'>
# print(type(True))
# # => <class 'bool'>
# print(type(10.4))
# # => <class 'float'>
#
# # Structurile de date
# # LISTA - MUTABILA adica putem sa modificam lista
#
# # Lista - Ordonata adica se poate accesa dupa index
# my_list = [1, 2, 3, 4, 5, True, 6.4, "barbat"]
# print(my_list[0])   # => accesarea primului element din lista -> 1
# print(my_list[-1])  # => barbat
# # inversarea unei liste
# print(my_list[::-1])  # => ['barbat', 6.4, True, 5, 4, 3, 2, 1]
# # lungimea listei
# print(len(my_list))   # => 8
#
# contacte = {
#     'Ana': '0722345678',
#     'Marius': '0721549888',
#     'Maria': '0765332967'
# }
# print(contacte["Marius"])  # => 0721549888
# # print(contacte['Alin'])    # => eroare: KeyError
# print(contacte.get("Alin", "nu este"))  # => nu este
# print(len(contacte))       # => 3 chei
#
#
# """# dorim sa accesam numarul lui Marius
# # accesam o valoare din dictionar furnizand cheia
# # asociata cu acea valoare"""
# print(contacte['Marius'])  # =>  0721549888
# """# dorim sa accesam numarul lui Alin
# # dorim sa accesam valoarea aferenta cheii Alin
# # -> DEZAVANTAJ: daca cheia nu exista in dictionar,
# # si folosim aceasta sintaxa => obtinem eroare"""
# # print(contacte['Alin']) # -> eroare: KeyError
# print("here")
#
# lista_mea = [1, 2, 3, 4, 5]
# lista_mea.append(6)  # Adaugă 6 la sfârșitul listei
# print(lista_mea)  # Afișează: [1, 2, 3, 4, 5, 6]
#
# my_tuple = (1, 2, 3, 4, 5, 2, 4)
# print(my_tuple[0])  # Afișează: 1
# print(len(my_tuple))  # Afiseaza 7
#
# my_set = {"apple", "banana", "cherry"}
# print(my_set.update(["blueberry"]))
# print(my_set)  # => {'banana', 'blueberry', 'cherry', 'apple'}
# print(my_set.pop())
# print(my_set)  # => {'blueberry', 'cherry', 'apple'}

# # WHILE
# i = 0
# while i <= 3:
#     i += 1
#     print(i)


# # WHILE ELSE
# i = 0
# while i <= 3:
#     i += 1
#     print(i)
# else:
#     print("Am iesit din loop")

# FOR
# executam functia print de 3 ori
# for i in range(4):
#     # i este o variabila care va reprezenta
#     # pe rand, fiecare valoarea din range(4)
#
#     # adica 0, 1, 2, 3
#     # in loc de i putem pune orice alt nume
#     # avem acces la variabila i doar in interiorul for-ului
#     print(i)

# # FOR ELSE
# for i in range(4):
#     print(i)
# else:
#     print("Am iesit din loop.")

# FOR EACH
# culori = ["rosu", "albastru", "galben", "mov"]
#
# for culoare in culori:
#     print(f"Culoarea mea preferata este {culoare}")

# CONTINUE
# for i in range(4):
#     # conditia pentru care vrem sa oprim iteratia
#     if i == 2:
#         # cand se indeplineste, va sari peste valoare
#         continue
#     print(i)

# Functii si parametrii


# def greet():
#     print("Hello")
#
#
# greet()   # =>Hello


def greet(name):
    if name == "Cosmin":
        return f"Domnul, {name}!"
    else:
        return f'Doamna, {name}!'


print(greet("Cosmin"))  # =>Domnul, Cosmin!

# Clasa


class Dog:
    # fields (atributtes)
    rasa = "Bischon"
    color = None
    year = 2024
    no_of_dogs = 0

    # constructor
    def __init__(self, color, name):  # parametrii
        self.__color = color
        self.name = name
        Dog.no_of_dogs += 1

    @property
    def culoare(self):
        print(f"Getter")
        return self.__color

    @culoare.setter
    def culoare(self, culoarea_noua):
        print(f'Setter: Noua culoare este: {culoarea_noua}')
        self.__color = culoarea_noua

    @culoare.deleter
    def culoare(self):
        print(f'Deleter: Am sters culoarea')

    #methods
    def speak(self):
        print("Ham-ham")

    def run(self):
        print("Running!")

    def __repr__(self):
        return f'Dog({self.rasa}, {self.culoare}, {self.name})'


# # initializam obiecte din clasa Dog
# obj_1 = Dog()   # => <__main__.Dog object at 0x00000281FF5029F0>
# obj_1.speak()  # dupa . avem acces la atribute si metode
# obj_1.run()  # => Running!
# print(obj_1.rasa)  # => Bischon
# obj_1.color = "alb"  # putem asocia sau suprascrie valori
# print(obj_1.color)   # => alb
# print(obj_1.year)    # => 2024
# obj_1.rasa = "Lup"
# print(obj_1.rasa)   # => Lup

# # initializam obiecte din clasa Dog
print(Dog.no_of_dogs)
dog1 = Dog("black", "Azorel")
dog2 = Dog("white", "Aisha")
# dog1.speak()  # =>Ham-ham
# dog1.run()    # =>Running
# print(dog1.rasa)  # =>Bischon
# print(dog1.color) # =>Black
# print(dog1.year)  # =>2024
# dog1.color = "rosu"
# print(dog1.color)
print(dog1.culoare)
dog1.culoare = "rosu"  # am setat culoarea rosu
print(dog1.culoare)  # => rosu
del dog1.culoare     # =>Deleter: Am sters culoarea
print(dog1.__dict__)  # =>{'_Dog__color': 'rosu', 'name': 'Azorel'}
dog1.culoare = "verde"
print(dog1.culoare)
print(dog1)  # => cu ajutorul metodei magice sau "dunder method" care reprezinta obiectul creat
print(Dog.no_of_dogs)
print(dog2)
##########################################
# FOR LOOP
for i in range(1, 11):
    print(f'Number: {i}')

##############################################
x = 5
def add():
    x = 3
    x = x + 5
    print(x)

add()
print(x)
