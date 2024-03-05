"""
FIND THE BUG!

Identifica eroarea din fiecare caz de mai jos

"""

# # 1: IndexError, list index out of range, linia 14
# nr_pare = []
# for i in range(1, 11): # i = 1 2 3 4 5 6 7 8 9 10
#     if i % 2 == 0:
#         nr_pare.append(i)
#
# print(nr_pare[5])

# nr_pare = [2, 4, 6, 8, 10]
# Eroarea apare pentru ca incercam sa accesam elementul de la indexul 5,
# iar ultimul index disponibil in lista nr_pare este 4.


# 2: KeyError, 'Departament', linia 35
# angajati = [
#     {
#         "nume": "Marc",
#         "prenume": "Paula",
#         "salariu": 3000
#     },
#     {
#         "nume": "Pop",
#         "prenume": "Alex",
#         "salariu": 4500,
#         "departament": "HR"
#     }
# ]
# print(angajati[1]["Departament"])

# o solutie sa nu mai avem eroare, este sa accesam valoarea cheii
# 'departament', si nu, 'Departament'.
# alta solutie: angajati[1].get("Departament", "Nu avem cheia respectiva")


# 3: ValueError, 'I/O operation on closed file', linia 45
# with open("scrisoare_recomandare.txt", mode="w") as f:
#     f.write("Aceasta este o scrisoare de recomandare!")
# f.read()

# Daca vrem sa citim continutul fisierului,
# punem f.read() intr-un nou bloc with, in care deschiderea fisierului
# se va face in modul read (mode="r")
# with open("scrisoare_recomandare.txt", mode="r") as f:
#     print(f.read())


# 4: TypeError, __init__() missing 3 required positional arguments: 'name', 'eyes_color', and 'height'
# class Person:
#
#     def __init__(self, name, eyes_color, height):
#         self.name = name
#         self.eyes_color = eyes_color
#         self.height = height
#

# class Student(Person):
#
#     def __init__(self, name, eyes_color, height, university):
#         super().__init__()
#         self.university = university
#
#
# student1 = Student("Ana Popa", "green", "170", "Universitatea Tehnica Cluj-Napoca")
# print(student1.eyes_color)
# print(student1.university)
# print(student1.name)

# pentru a rezolva eroarea, la linia 66 trebuie sa adaugam argumente pentru
# name, eyes_color si height, atunci cand apelam constructorul din clasa parinte.
# super().__init__(name, eyes_color, height)

# 5: AttributeError, 'Student' object has no attribute 'age', linia 98
# class Person:
#
#     def __init__(self, name, eyes_color, height):
#         self.name = name
#         self.eyes_color = eyes_color
#         self.height = height
#
#
# class Student(Person):
#
#     def __init__(self, name, eyes_color, height, university):
#         super().__init__(name, eyes_color, height)
#         self.university = university
#
#
# student1 = Student("Ana Popa", "green", "170", "Universitatea Tehnica Cluj-Napoca")
# print(student1.eyes_color)
# print(student1.university)
# print(student1.age)
# print(student1.name)

# Ca rezolvare, fie nu mai accesam valoarea atributul age, avand in vedere ca
# nu este disponibil pe obiectele din clasa Student,
# fie adaugam acest atribut in cosntructor (ori in constructorul clasei Student,
# ori in costructorul clasei Person - recomandare: in costructorul clasei Person,
# pentru ca age este un atribut/o proprietate care ar trebui sa caracterizez orice obiect
# din clasa Person/ orice persoana.

# 6 AttributeError: 'User' object has no attribute '__password', linia 119
class User:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password


user1 = User("anapopa25", "ana.popa@gmail.com", "123abc")
print(user1.username)
print(user1.__password)
print(user1.email)

# posibile rezolvari:

# v1: Nu mai accesam atributul __passoword in exterioul clasei

# v2: In loc sa facem atributul __password sa fie privat, il putem facem sa fie
# protected, punand un singur _ in fata denumirii: _password.
# In acest fel, atributul poate fi accesat din exterior dar dam de inteles (pentru alti programatori)
# ca acest atribut nu ar trebui sa fie folosit/accesat in exteriorul clasei.

# v3: folosirea unei proprietati pe care definim getter-ul.
