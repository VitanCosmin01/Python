"""
1. Explica intr-un comentariu ce este o variabila de tip string.
o variabila de tip string este un sur de caractere delimitat de ghilimele simple sau duble
si este ordonat si imutabil.
"""
from colorama import Fore

"""
2. Defineste 3 variabile: oras, strada si nr.
a. Afiseaza aceste variabile intr-o propozitie, folosind concatenarea string-urilor.
b. Afiseaza aceste variabile intr-o propozitie, folosind f-strings.
"""
# oras = 'Blaj'
# strada = 'Iazului'
# nr = '9A'
# print('Eu locuiesc in orasul ' + oras + ' pe strada ' + strada + ' la numarul ' + nr + '!' )
# print(f'Eu locuiesc in {oras}, pe strada {strada}, la numarul {nr}!')
"""
3. Se da variabila string, nume_complet = 'Pop Maria Ioana'.
a. Afiseaza numele de familie din string.
b. Afiseaza al doilea prenume.
c. Afiseaza de cate ori apare litera 'a' in nume_complet.
d. Inverseaza string-ul si afiseaza rezultatul.
e. Inlocuieste al doilea prenume cu 'Elena'.
f. Afiseaza caracterele de la indexul 5 la indexul 9 (inclusiv).
g. Afiseaza caracterele de la inceputul string-ului pana la index-ul 8 (inclusiv).
"""
# a
# nume_complet = 'Pop Maria Ioana'
# # b
# print(nume_complet[:3])
# # c
# print(nume_complet[4:10])
# # d
# print(nume_complet[::-1])
# # e
# print(nume_complet.replace('Maria', 'Elena'))
# # f
# print(nume_complet[4:10])
# # g
# print(nume_complet[:8])


"""
4. Citeste de la tastatura culoarea preferata a utilizatorului si salveaza rezultatul intr-o variabila.
a. Determina lungimea inputului citit de la tastatura.
b. Determina tipul inputului citit de la tastatura.
c. Transforma inputul de la utilizator in text cu litere mari si afiseaza-l.
d. Transforma inputul de la utilizator in text care incepe cu litera mare si restul sunt litere mici.
Afiseaza rezultatul.
"""
#input(print('Culoare preferata este?'))

# for culoare in culori:
#     print('Culoarea preferata este:')
#     input()

"""
5. Se da variabila anotimp = 'primavara'. Verifica daca anotimp se termina in 'vara'.
"""
# anotimp='primavara'
# if anotimp.endswith('vara'):
#     print(True)
# else:
#     print(Fals)
"""
6. Citeste de la tastatura pretul cosului de cumparaturi. Afiseaza pretul cu un discount de 25%.
"""
# cos = int(input("Introdu valoarea cosului de cumparaturi: "))
# discount = 15/100
# oferta = cos - (cos * discount)
# print(oferta)
"""
7. Se da string-ul: zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'.
Transforma string-ul in lista, folosindu-te de o metoda ajutatoare de pe string.
"""

# zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'
# lista = zile_sapt.split(sep=',')
# print(lista)  #  ['luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica']

"""
8. Scrie un program care solicita utilizatorului sa introduca varsta sa
și returneaza un mesaj personalizat, in funcție de varsta introdusa.
Daca varsta este mai mare sau egala cu 18, programul trebuie sa afiseze
mesajul "Esti major si poti vota".
In caz contrar, programul trebuie sa afiseze mesajul "Esti minor si nu poti vota inca".
"""

"""
9. Scrie un program care primeste un pret de la tastatura si afiseaza
un mesaj daca prețul este mai mare sau mai mic decât 100 de lei.
"""

"""
10. Citeste doua numere intregi de la tastatura. Printeaza produsul dintre cele doua numere
daca acesta este mai mic sau egal decat 1000, altfel printeaza suma lor.
"""
# num_1 = int(input("introdu primul numar: "))
# num_2 = int(input("introdu al 2-lea numar: "))
# produsul = num_1 * num_2
# suma = num_1 + num_2
# if produsul <= 1000:
#     print("Produsul numerelor este" + " " + str(produsul))
# else:
#     print(f'Suma acestora este {suma}')
"""
11. Se dau doua liste:
lista_1 = [10, 20, 30, 40, 50, 10]
lista_2 = [1, 2, 3, 4, 5]
Pentru fiecare lista verifica daca primul si ultimul element sunt egale.
In functie de rezultat, afiseaza un mesaj.
"""
# lista_1 = [10, 20, 30, 40, 50, 10]
# lista_2 = [10, 2, 3, 4, 5]

# varianta 1
# x = lista_1[0]
# print(x)
# y = lista_2[0]
# print(y)
# if x == y:
#     print('Primele elemente din fiecare lista sunt egale')
# else:
#     print('Primele elemente ale listelor sint diferite')
# varianta 2
# if lista_1[0] == lista_2[0]:
#     print('Primele elemente din fiecare lista sunt egale')
# else :
#     print('Primele elemente ale listelor sint diferite')

"""
12. Scrie un program care afiseaza de cate ori apare litera 'e' in
stringul str_1 = 'Emma is a sofware developer.'
"""
# str_1 = 'Emma is a sofware developer.'
# print(str_1.count('e'))
"""
13. Scrie un program in care citesti de la tastatura doua nr intregi,
numite base si exponent.
Afiseaza intr-un mesaj sugestiv, valoarea lui base la puterea exponent.
Atentie: indiferent daca utilizatorul a introdus un numar pozitiv sau negativ
ca si exponent, trebuie sa ridici base la puterea exponent pozitiv.
hint: exploreaza functia abs() si vezi cum o poti folosi
"""
# base = int(input('base '))
# exponent = int(input('exponent '))
#
# rezultat=base**exponent
# print(f'Rezultatul este {rezultat}')


"""
14. Scrie un program in care se citeste de la tastatura un string.
Daca string-ul are numar impar de caractere, afiseaza un string care
contine primul caracter, caracterul din mijloc si ultimul caracter
al string-ului citit de la tastatura.
Daca string-ul are numar par de caractere, afiseaza un string care contine doar primul
si ultimul caracter  al string-ului citit de la tastatura.
"""
# x = input('Introdu un cuvant ')
# print(x[])
# #print(type(x))
# #print(int.len(x))) % int(0)
# #print(type(x)

# if x.count() % 0:
#     print(acasa)

"""
15. Se dau doua variabile:
str1 = 'Abc'
str2 = 'Xyz'
Creeaza o variabila string, str3 formata din:
- primul caracter din str1 cu litera mica
- primul caracter din str2 cu litera mare
- al doilea caracter din str1 cu litera mare
- al doilea caracter din str2 cu litera mare
- al treilea caracter din str1 cu litera mare
- al treilea caracter din str2 cu litera mica
"""
# str1 = 'Abc'
# str2 = 'Xyz'
# str3 = str1[0].lower() + str2[0].capitalize() + str1[1].capitalize() + str1[2].capitalize() + str2[2].lower()
# print(str3)   #  aXBCz

"""
16. Se da lista:
fruits = ["apple", "banana", "cherry"]
a. Schimba elementul 'apple' cu 'kiwi'.
b. Foloseste metoda append() pentru a adauga elementul 'oranges'.
c. Foloseste metoda insert() pentru a adauga elementul 'lemon' ca al doilea
element din lista.
d. Foloseste metoda remove() pentru a sterge elementul 'banana' din lista.
e. Foloseste un index negativ pentru a accesa ultimul element din lista.
f. Foloseste un index negativ pentru a accesa penultimul element din lista.
g. Afiseaza lungimea listei.
h. Foloseste slicing pe lista, astfel incat sa obtii o lista cu al doilea, al treilea
si al patrulea element.
"""
# fruits = ["apple", "banana", "cherry"]
# fruits[apple] = "kiwi"
# print(fruits)
"""
17. Inverseaza lista my_list = [100, 200, 300, 400].
"""

"""
18. Lista de cumparaturi:
Se citeste de la tastatura o lista de cumparaturi. Utilizatorul introduce
lista de cumparaturi ca un string, cu alimentele separate prin virgula,
ATENTIE: fara spatii
Exemplu:rosii,castraveti,branza,oua
a. Sa se transforme string-ul citit de la tastatura intr-o lista. 
(vezi metode ajutatoare string).
b. Sorteaza lista de cumparaturi si printeaza lista sortata.
c. Adauga un aliment nou in lista de cumparaturi.
d. Sterge un aliment din lista de cumparaturi.
e. Modifica elementul de la pozitia 0 din lista.
f. Daca lista contine 'rosii' in ea, afiseaza mesajul "Aliment sanatos".
Daca nu, afiseaza mesajul "Iti recomandam rosiile de asemenea".
"""
# lista_cumparaturi='rosii,castraveti,branza,oua'
#
# print(lista_cumparaturi.split())  # ['rosii,castraveti,branza,oua']
# lista_sortata = sorted(lista_cumparaturi)
# print(lista_sortata) # [',', ',', ',', 'a', 'a', 'a', 'a', 'a', 'b', 'c',
# 'e', 'i', 'i', 'i', 'n', 'o', 'o', 'r', 'r', 'r', 's', 's', 't', 't',
# 'u', 'v', 'z']
# nu stiu sa fac asta
"""
19. Se da lista fructe = ['capsuni', 'mere', 'lamai'].
Converteste lista la string si afiseaza string-ul. A se vedea metoda join(). 
(search on google)
"""
# fructe = ['capsuni', 'mere', 'lamai']
# str = str   (fructe)
# print(help(list))


#print(dir.join)
"""
20. Se da lista numere = [1, 2, 3, 4, 56, 22, 5].
Afiseaza elementul cu valoarea maxima din string. (google- functia max())
"""
# numere = [1, 2, 3, 4, 56, 22, 5]
# print(max(numere))
"""
21. Se da lista preturi = [12.3, 34.5, 22].
Calculeaza suma elementelor din lista preturi. (google - functia sum())
"""
# preturi = [12.3, 34.5, 22]
# print(sum(preturi))
"""
22. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza valoarea cheii city.
b. Kelly a fost promovata. Salariul ei este acum de 10000 lei. Fa modificarea si in dictionar.
c. Sterge varsta din dictionar.
d. Adauga o noua pereche cheie-valoare in dictionar, cu cheia employment_date. Valoarea o alegi tu.
e. Verifica daca exista cheia 'country' in dictionar. Daca nu exista, adauga-o.
"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# print(sample_dict["city"])      # a
# sample_dict["salary"] = 10000
# print(sample_dict["salary"])   #  b
# sample_dict.pop("age")
# print(sample_dict)              #  c
# sample_dict.update({"emploiment_date": "15.01.2024"})
# print(sample_dict)              #  d
# print(sample_dict.get("country"))
# sample_dict.update({"country": "Romania"})
# print(sample_dict)              #  e

"""
23. Se da dictionarul:
sample_dict1 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza toate cheile din dictionar. (HINT: metoda keys())
b. Afiseaza toate valorile din dictionar. (HINT: metoda values())
c. Verifica lungimea dictionarului.
"""
sample_dict1 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# print(sample_dict1.keys())
# print(sample_dict1.values())
# print(len(sample_dict1))
"""
24. Gasirea unui element intr-un dictionar
Se da dictionarul:
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul introduce cheia cautata.
Verifica daca aceasta se gaseste sau nu in dictionar.
"""
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
# searched_key = str(input("Introdu cheia cautata: "))
# print(persoana.get(searched_key))

"""
25. Adaugarea unui element intr-un dictionar
Se da dictionarul:
 persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul trebuie sa introduca cheia si valoarea pe care doreste sa
le adauge in dictionar.
Foloseste metoda update() (metoda ajutatoare pe dictionar)
"""
persoana1 = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
# persoana1.update({"inaltime": 171})
# print(persoana1)
"""
26. Stergerea unui element din dictionar
 Se da dictionarul:
 persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul introduce cheia elementului de eliminat.
a. Elimina elementul, verificand prima data daca cheia se afla in dictionar,
si daca se afla, foloseste metoda del.
b. Elimina elementul, folosind metoda ajutatoare pop().
"""
# del_key = str(input("Elimina cheia: "))
# if persoana1.get(del_key) is not None:
#     print(persoana1)
#     del persoana1[del_key]
# print(persoana1)

# 27. Concatenarea a doua dictionare.
# Se dau doua dictionare:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# Sa se concateneze cele doua dictionare folosind metoda update().
# Observatie: Metoda update() o putem folosi pentru a adauga unul sau mai multe
# perechi cheie:valoare in dictionar.



# # 28. Se da urmatoarea lista cu dictionare:
# lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
# # a. Adauga perechea {'c':'3'} in primul dictionar din lista.
# lista[0].update({"c": 3})
# print(lista)
# # b. Adauga un nou dictionar ca element in lista. Adauga-l la final.
# lista.append({"g": 7})
# print(lista)
# # c. Adauga un nou dictionar ca element in lista, la indexul 1.
# lista.insert(1,{"h": 8})
# print(lista)
# # d. Verifica daca in al doilea dictionar din lista se gaseste cheia 'c'.
# lista[1].get("c")
# print(lista)
"""
29.
Se citeste de la tastatura un numar.
a. Printeaza un mesaj sugestiv daca numarul este par sau nu.
b. Daca numarul este multiplu de 4, afiseaza un mesaj sugestiv.
"""
# user_number = int(input("Introdu un numar: "))
# if user_number % 2 == 0:
#     print("Numarul este par")
# else:
#     print("Numarul este impar")
# if user_number % 4 == 0:
#     print("Numarul este multiplu de 4")
# else:
#     print("Numarul nu este multiplu de 4")
"""
30.
Se citesc de la tastatura doua numere, num si check. Verifica daca
num este divizibil cu check si afiseaza un mesaj corespunzator catre utilizator.
"""
# num = int(input("Introdu un numar intreg: "))
# check = int(input("Introdu un numar intreg, divizorul: "))
# if num >= check and num % check == 0:
#     x = num / check
#     print(x, "-Num se divide cu check")
# else:
#     print(num % check, "Operatie imposibila")
# # 31. Se da dictionarul:
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# a. Foloseste metoda get() pentru a printa valoarea cheii 'model'.
# print(car.get("model"))
# b. Schimba valoarea cheii 'year' in 1970.
# car["year"] = 1954
# print(car.get("year"))
# c. Adauga perechea cheie:valoare 'color':'red' in dictionar.
# car.update({"color":"red", "Inmatriculat": True})
# print(car)
# Adaug-o folosind accesarea dictionarului prin cheie (car['color']) si dand o valoare.
# car["color"] = "red"
# print(car["color"])
# Adaug-o folosind metoda update()
# d. Foloseste metoda pop() pentru a sterge 'model' din dictionar.
# car.pop("model")
# print(car)
# e. Foloseste metoda empty() pentru a 'goli' dictionarul.
# car.clear()
# print(car )

'''
#  sololearn
You are given a list of contacts, where each contact is represented by a tuple, 
with the name and age of the contact.
Complete the program to get a string as input, search for the name in the list of 
contacts and output the age of the contact in the format presented below:

Sample Input:
John

Sample Output: 
John is 31

If the contact is not found, the program should output "Not Found".
'''
# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
#     ]

# name = input("Introdu  numele: ")
# for contact in contacts:
#     contact_name = contacts[:][0]
#     age = contacts[:][1]
#     if name in contact:
#         print(f'{contact_name} is {age}')
#         break
#     else:
#         print("Not found")
# name_1 = input()
# for contact in contacts:
#     if contact[0] == name_1:
#         age = contact[1]
#         print(f'{name_1} is {age}')
#         break
#     else: print('Not Found')   # here is the hell of the code and it took me almost all my day to figure it out




# my_string = "python"
# x = 0
#
# for i in my_string:
#     x = x + 1                 # atribuim lui x o valoare crescanda
#     print(my_string[0:x])
# for i in my_string:
#     x = x - 1                   # atribuim lui x o valoare in scadere
#     print(my_string[0:x])

'''
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
    if i == 4:
        break
    else:
        print(Fore.RED + "0")
'''
#
# names = ["Tim", "James", "Steve"]
# names.append(2, "Bill")
# print(names)

# Car entity
# class Car:
#     def __init__(self, model,brand, year):
#         self.__details = {
#             'model': model,
#             'brand': brand,
#             'year': year
#         }
#     def get_brand(self):
#         return self.__details['brand']
#
# garage = [Car('Model S', 'Tesla', 2020), Car('Corolla','Toyota', 2019)]
#
# print(garage[0].get_brand())      # Raspuns: Tesla

"""
EX2: Calcularea mediei
Ne dorim sa cerem utilizatorului sa introduca notele
luate la examene. 
Vom lua input-ul de la utilizator, pana
cand acesta introduce -1.
In functie de notele luate, trebuie sa calculam media aritmetica
si sa o afisam.
"""
nota = int(input("Introdu nota: "))
list_note = []
while nota >= 10:
    list_note.append(nota), nota
    elif nota == -1:

media = sum(list_note) / len(list_note)
print(media)





