'''
x = 4
y = 2
print(x % y)  #=> afiseaza restul impartirii
print(x - y)
print(x**y)   #=> ridicarea la putere
print(x // y)  #=> face operatia de impartire si afiseaza numarul intreg
mystr='s'
print(mystr*3)
print(4/2)
print(x>y)
print(x>y and x<4) # daca e True si Fals = Fals
print(x>y or x<y)  # True or Fals = Fals
'''
# IF
# x=5
# if  x==5:
#     print('x este egal cu 5')
#     print('si asta')
# else:
# #     print('x nu este egal cu 5')
# nota_de_trecere = 10
# nota = int(input('scrie nota '))
# if nota<7 and nota>=5:
#     print('premiul 3')
# elif nota>7 and nota<=9:
#     print('premiul 2')
# elif nota>9:
#     print('premiul 1')
# else:
#     print('ai picat examenul')


# sample = [10, 20, 30, 40, 50]
# sample.append(60)
# print(sample)
#
# sample.append(60)
# print(sample)
#
# numbers = [1, 5, -7, -12, 10]
# print(max(numbers), end=',')
# print(min(numbers), end=',')
# print(len(numbers))
#
# my_lyst = [10, 20, 30, 40, 50]
# my_lyst.pop()
# print(my_lyst)
#
# my_lyst.pop(2)   # in paranteze se foloseste indexu-ul care porneste de la 0
# print(my_lyst)   # porneste de la 0

# my_lyst = [5, 10, 15, 25]
# print(my_lyst[::-2]) # afiseaza lista in ordine inversata, de la primul element din 2 in 2

# colors_set = {'red', 'green', 'blue'}
#
# colors_set.add('orange')
# colors_set.add('red')
#
# print(colors_set)  # in seturi nu se permit elemente dublicate

# my_dict = {
#     'name': 'Mihai',
#     'salary': '10000'
# }
#
# print(my_dict['age'])  # nu se poate printa un element care
#                        # nu face parte din dictionar
# my_dict = {
#     'name': 'Mihai',
#     'salary': '10000',
#     'age':37
# }
#
# print(my_dict['age'])

# for i in range(1, 5):
#
#     print(i)  #  afiseaza 1 2 3 4 una sub alta
#
# stoc_fructe = ['lamai', 'portocale', 'capsuni', 'cirese']
# for fruct in stoc_fructe:
#     if fruct == 'capsuni':
#         print('Am gasit fructele mele preferate!')
#         break
# else:
#     print('Nu am gasit fructele mele preferate!')

# result_list = []
# for number in range(0, 6):
#     if number == 3 or number == 4:
#         continue
#     result_list.append(number)
#     print(result_list)

# def print_hi():
#     print('Hello')
#
# print_hi()

'''''
def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print('Sorry! You are dividing by zero!')
    else:
        print('Yeah! Your answer is :', result)
    finally:
        print('This is always executed!')

#divide(3, 2)
divide(3, 0)
'''''
'''''
class Car:
    # fields/atributes
    make = 'Dacia'
    model = 'Sandero'
    year = 2022
    color = 'white'


    # constructor
    def __init__(self, model, color):
        self.make = model
        self.color = color

car1 = Car('Duster', 'white')
car2 = Car('Logan', 'blue')
print(car1.make)
print(car1.model)
print(car1.color)
 ''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.

2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
  '''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# varianta 1
# for masina in masini:
#     print(f'Mașina mea preferată este {masina}')

# varianta 2

# while masina in masini:
#     print(f'masina mea preferata este {masina})


# each = 'Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'
# print(each)

"""
EX2: Calcularea mediei
Ne dorim sa cerem utilizatorului sa introduca notele
luate la examene. 
Vom lua input-ul de la utilizator, pana
cand acesta introduce -1.
In functie de notele luate, trebuie sa calculam media aritmetica
si sa o afisam.
"""
''''
# inițializăm lista de note
note = []
# inițializăm nota cu primul input de la utilizator
nota = int(input("Introduceți nota (introduceți -1 pentru a încheia lista de note): "))
# citim toate notele până când utilizatorul introduce -1
while nota != -1:
    note.append(nota)
    nota = int(input("Introduceți nota (introduceți -1 pentru a încheia lista de note): "))
# calculăm media aritmetică
media = sum(note) / len(note)
# afișăm media
print("Media notelor este:", media)

'''
# i = int(input('Introdu nota '))
# for i in range(1, 11):
#     i = int(input('Introdu nota '))
#
#     break

"""
EX5:
2. Se da lista:
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]
Sa se afiseze toate produsele care au pretul mai mare de 5 lei.



produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]
"""
#
# list1 = ["abc", 34, True, 40, "male", "male"]
# list1.insert(2, 'cafea')
# #print(list1)
# list1.append('ap')

# functie cu parametri care nu returneaza nimic

# functie cu doi parametri
# def add_numbers(a, b):
#     result = a + b
#     print(f'Sum: {result}')
#
# add_numbers(1, 2)
# add_numbers(3, 4)
#
# def print_hi():
#     print('Helloooo')
#
# print_hi()
#
# def add_numbers(a + b):
#     sum = a + b
#     print(f'Suma este de {sum} lei')
# add_numbers(7+ 6)
# ''''''''''''''''''''''''
# class Animal:
#     tip = 'caine'
#     gen = 'mascul'
#     culoare = 'negru'
#     varsta = 2
#
#     def caracteristici(self):
#         print(f'Bietul {self.tip} este de culoare {self.culoare} si este acasa!')
#
# print(Animal.tip)
#
# def first_function():
#     print("Hello World!")
#
# '''''''''''''''''''''''''''################################
# i = 0
# while i  <= 8:
#     print(i)
#     i += 1
##############################################################
"""
EX1: MOSTENIRE
a. Defineste o clasa numita Persoana.
Aceasta clasa va avea urmatoarele atribute (in constructor):
- nume
- varsta

Implementeaza metoda descrie(), care va afisa mesajul:
'Persoana {nume} are {varsta} ani.'

b. Defineste clasa Angajat, care mosteneste din clasa Persoana.
Aceasta clasa va lua in constructor inca doi parametri,
salariu si post.
Defineste metoda afiseaza_salariu, care returneaza
atributul salariu.

c. Creeaza un obiect de tip clasa Persoana.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metoda descrie.

d. Creeaza un obiect de tip Angajat.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metodele disponibile pe aceasta.

e. Extinde metoda descrie din clasa Angajat,
astfel incat sa se afiseze
si o propozitie care contine atributele salariu si post.
"""


# class Persoana:
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#     def describe(self):
#         print(f'Persoana {self.nume} are varsta de {self.varsta} ani!')
#
# # class Angajat(Persoana):
# #     def __init__(self, nume, varsta, salariu, post):
# #         super().__init__(salariu, post)
# #         self.salariu = salariu
# #         self.post = post
# #
# #     def afiseaza_salariu(self):
# #         return self.salariu
# #
# # salar = Angajat.afiseaza_salariu(49)
# class Angajat(Persoana):
#     def __init__(self, nume, varsta, salariu, post):
#         super().__init__(nume, varsta)
#         self.salariu = salariu
#         self.post = post
#
#     def show_salariu(self):
#         return self.salariu
#
#
# pers1 = Persoana('Cosmin', 40)
# print(pers1.nume)
# print(pers1.varsta)
# pers1.describe()
#
# pers1 = Angajat('Cosmin', 40, 5000, 'tehnician')
# print(pers1.salariu)
# print(pers1.post)
##############################################
# Exemplu de class methods polimorfice
class Romania:
    def language(self):
        print("Romanian")


class USA:
    def language(self):
        print("English")


obj_ro = Romania()  # se creeaza obiectul "obj_ro" ( se atribuie obiectului o functie sau atribut )
obj_usa = USA()

obj_ro.language()  # se invoca sau se actvizeaza  functia(language) obiectului(obj_ro)
obj_usa.language()

"""
EX2: POLIMORFISM

a. Defineste o clasa Pasare care implementeaza metoda 
zboara.
In metoda zboara, afiseaza mesajul 'Majoritatea pasarilor
pot zbura.'

b. Defineste o clasa Strut, care mosteneste din clasa 
Pasare.
Defineste metoda zboara, si afiseaza mesajul 
'Strutii nu pot zbura."
(Nu extindem metoda din clasa de baza, 
ci o suprascriem -> OVERRIDING)

c. Defineste clasa Rata, care mosteneste din clasa Pasare.
Defineste metoda zboara, si afiseaza mesajul 
"Ratele pot zbura."

d. Instantiaza cele 3 clase si apeleaza metoda zboara
pe fiecare obiect.
POLIMORFISM => aceeasi metoda (acelasi nume) -> 
comportament diferit.
"""


# class Pasare:
#     def zboara(self):
#         print(f'Majoritatea pasarilor pot zbura!')
#
# # class Strut(Pasare):
# #     def zboara(self):
# #         print(f'Strutii nu pot zbura!')
# class Strut(Pasare):
#     def __init__(self):
#         super().zboara(self)
#         print(f'Strutii nu pot zbura')

#
#
# pasarica = Pasare()
# pasarica.zboara()
# strut = Strut()
# strut.zboara()
##########################
class Car:
    make = 'Dacia'
    model = None
    year = 2023
    color = None

    def __init__(self, model, color):
        self.model = model
        self.color = color


car1 = Car('duster', 'white')
print(car1.color)
print(car1.make)
print(car1.model)
print(car1.year)

# Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)


a = {
    "marca": "Dacia",
    "model": 1300
}

print(len(a))

#####################################