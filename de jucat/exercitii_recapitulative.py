my_list = ["rosu", "castron", 1]

# ordonata
print(my_list[1])

# mutabila
my_list.append(3.4)
print(my_list)

# variabile/constante

# variabile

numar = 1
numar += 2
print(numar)

numar = 10

# constante
LINK = "https://www.google.com"

my_dict = {
    "nume": "Ana Popa",
    "varsta": 20
}

# dictionarul este neordonat -> nu putem accesa elementele dupa index
# dictionarul este mutabil -> elementele sale pot fi modificate
# my_dict["nume"] = "Maria Popa"
# print(my_dict)

# string-ul este IMUTABIL
# my_str = "abcaaa"
# print(my_str.replace("a", "1"))
# print(my_str)
#
# # string-ul este ORDONAT
# print(my_str[2])
#
# print(my_str[0:3]) # abc
# print(my_str[:3]) # abc
#
# print(my_str[3:]) # aaa
# print(my_str[3:-1]) # aa


# pe dictionar avem disponibila metoda clear
my_dict.clear()
print(my_dict)

# print(my_dict["key1"])

# list1 = []
# print(list1[0])

# x = 75
#
# def my_func():
#     x = x + 1
#     print(x)
#
# my_func()
#
# print(x)
"""
Exercitii recapitulative
"""

"""
1. Creaza o functie Python care inversează și returnează un număr întreg pozitiv.
În cazul unui număr negativ, afișează o eroare.

Exemple: 
reverse(1234567) => 7654321
reverse(10) => 1
reverse(101) => 101
reverse(10000000) => 1
reverse(-65) => eroare -> ValueError
"""
# n = int(input('Introdu un numar:\n'))

# def reverse(numar):
#
#     if numar >= 0:
#         x = str(numar)
#
#         reversed = x[::-1]
#         return reversed
#     else:
#         raise ValueError('Numarul este negativ')
#         #print(f'numarul {numar} este negativ')
#
# print(reverse(n))


# varianta Flavius

# def rev(x):
#     if x >= 0:
#         a = str(x)
#         b = a[::-1]
#         c = int(b)
#         return c
#     else:
#         raise ValueError("Numarul NU este pozitiv")
#
# print(rev(-123486))


"""j = [3,2,1,41,23,1]
rev_j = reversed(j)
print(rev_j)
for n in rev_j:
    print(n)"""
# print("Mc'Donalds")
"""
2. Creaza o functie Python care primește o lista și un număr 
întreg pozitiv k, si roteste lista cu k pozitii.
 
Exemple:
rotate([1, 2, 3, 4, 5], 2) => [3, 4, 5, 1, 2]
rotate([1, 2, 3, 4, 5], 4) => [5, 1, 2, 3, 4]
rotate([1, 2, 3, 4, 5], 8) => [4, 5, 1, 2, 3]
rotate([1, 2, 3, 4, 5], 5) => [1, 2, 3, 4, 5]
rotate([1, 2, 3, 4, 5], 6) => [2, 3, 4, 5, 1]
rotate([1, 2, 3, 4, 5], 7) => [3, 4, 5, 1, 2]
"""
# varianta corecta


# def rotate(lista, k):
#     k = k % len(lista)
#     lista_v2 = lista[k:] + lista[0:k]
#     print(lista_v2)
# varianta Dragos dar inversa
# def rot(lst, n):
#     for i in range(n):
#         lst.insert(0, lstpop())
#     return lst
#
# my_list = [1, 2, 3, 4, 5]
# rotlst = rot(my_list, 1)
# print(rotlst)

# varianta Huminic Cosmin
# from collections import deque
#
# # varianta 1 Huminic
# def lista():
#     x = int(input("Introduceti numarul de elemente din lista:"))
#     our_list = deque([])
#     for i in range(x):
#         elements = input("Elementul" + str(i) + "este:")
#         our_list.append(elements)
#     return our_list
#
#
# our_list = lista()
# print(our_list)
# k = int(input("Introduceti numarul de rotatii dorit:"))
# our_list.rotate(-k)
# print(our_list)

# varianta 2 Huminic
# def rot(lista,k):
#     deque_list = deque(lista)
#     deque_list.rotate(-k)
#     return list(deque_list)
#
# print(rot([1,2,3,4,5],2))


"""
3. Creaza o functie Python care primește 2 stringuri, și verifica dacă acestea sunt anagrame (case-insensitive).

Exemple:
is_anagram(‘Adela’, ‘ealad’) => True
is_anagram(‘ITFactory’, ‘acfiorty’) => True
is_anagram(‘Stringy’, ‘gringsty’) => False
is_anagram(‘ana’, ‘ioana’) => False
"""

# varianta Farcas
# def is_anagram(cuvant1, cuvant2):
#     if (sorted(cuvant1.upper()) == sorted(cuvant2.upper())):
#         print("Sunt anagrams.")
#     else:
#         print("The strings aren't anagrams.")
#
#
# cuvant1 = input("string1 =  ")
# cuvant2 = input("string2 = ")
# is_anagram(cuvant1, cuvant2)
# varianta Huminic
# from collections import Counter
#
#
# def check(str1, str2):
#     if Counter(str1.lower()) == Counter(str2.lower()):
#         print("The strings are anagrams.")
#     else:
#         print("The strings aren't anagrams")
#
#
# str1 = "Cosmina"
# str2 = "animocs"
# check(str1, str2)

"""
4. Creaza o functie Python care primeste o lista de numere, si il returneaza pe al doilea cel mai mare numar distinct.

Exemple:
get_second_biggest([1,2,3,4,5]) => 4
get_second_biggest([1,2,3,4,4]) => 3
get_second_biggest([1,2,4,4,4]) => 2
get_second_biggest([-1,-2,-3,-4,-5]) => -2
"""
# listx = [1, 5, 4, 2, 9]
#
#
# def get_second_biggest():
#     sort = sorted.listx
#     print(sort)
#
# get_second_biggest()

"""
5. Creaza o functie Python care primeste doua stringuri ce 
reprezinta niste numere foarte mari,si returneaza rezultatul 
adunarii “numerelor”, tot sub format string:

Exemple:
add_two(‘12345’, ‘12345’) => ‘24690’
add_two(‘1234’, ‘4321’) => ‘5555’
add_two(‘563895634’, ‘548967348053’) => ‘549531243687’
"""


"""
6. Creaza o functie Python care primeste un numar n, si o 
lista de numere de dimensiune n-1.
In lista se afla toate numerele de la 1 la n, in afara de 1.
Functia trebuie sa gaseasca acel numar in cel mai eficient 
mod posibil si sa-l returneze.

Exemple:
find_missing(5, [1,2,3,5]) => 4
find_missing(2, [1]) => 2
find_missing(7, [6,5,1,3,2,7]) => 4
"""

"""
7. Creaza o clasa Calendar, care primeste ca unic parametru 
un an, si genereaza “calendarul” acelui an.
Se va tine cont de faptul daca anul este bisect sau nu.
Metode:
-> init(an) 
-> print_calendar(luna) - va printa calendarul pentru luna 
menționată intr-un format user-friendly, ex

October 2022
Mo 	Tu 	We 	Th 	Fr 	Sa 	Su
1 	2
3 	4 	5 	6 	7 	8 	9
10 	11 	12 	13 	14 	15 	16
17 	18 	19 	20 	21 	22 	23
24 	25 	26 	27 	28 	29 	30
31

-> get_day_of_week(zi, luna) - va returna ce zi din saptamna 
este, exemplu ‘Marti’
-> get_days_in_month(luna) - va returna numarul de zile din 
luna respectivă;
"""
# import calendar
# year = 2012
# mounth = 12
# print(calendar.month(year, mounth))


