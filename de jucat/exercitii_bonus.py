"""
1. Explicable intr-un comentariu ce este o variabila de tip string.
"""
# variabila este un container de memorie care stocheaza valori iar cel
# de tip string este un sir de caractere delimitat de '' sau ""
"""
2. Defineste 3 variabile: oras, strada si nr.
a. Afiseaza aceste variabile intr-o propozitie, folosind concatenarea string-urilor.
b. Afiseaza aceste variabile intr-o propozitie, folosind f-strings.


"""
# oras = 'blaj'
# strada = 'Iazului'
# nr = 9
# # a
# print('eu locuiesc in ' + oras + ' ' + ' ' + strada + ' ' + str(nr))
# # b
# print(f'Eu locuiesc in {oras} {strada} {nr}.')


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
# nume_complet = 'Pop Maria Ioana'
# # a
# print(nume_complet[:3])
# # b
# print(nume_complet[10:])   #imi afiseaza de la caracterul 10 inclusiv de la stanga la dreapta
# print(nume_complet[-5:])   #imi afiseaza primele 5 caractere de la dreapta la stanga
# c
# d
# print(nume_complet[::-1])
# # e
# print(nume_complet.replace('Maria', 'Elena'))
#
# # f
# print(nume_complet[4:10]) #afiseaza de la indexul 5 la 9
# # g
# print(nume_complet[:9])
"""
4. Citeste de la tastatura culoarea preferata a utilizatorului si salveaza rezultatul intr-o variabila.
a. Determina lungimea inputului citit de la tastatura.
b. Determina tipul inputului citit de la tastatura.
c. Transforma inputul de la utilizator in text cu litere mari si afiseaza-l.
d. Transforma inputul de la utilizator in text care incepe cu litera mare si restul sunt litere mici.
Afiseaza rezultatul.
"""
# var1 = "minge"
# var2 = "rosie"
# print(var1+var2)
# print(f'{var1}   {var2}')
"""
5. Se da variabila anotimp = 'primavara'. Verifica daca anotimp se termina in 'vara'.
"""
# anotimp = 'primavara'
# if anotimp.endswith('vara'):
#     print(f'cuv se termina cu vara')

"""
6. Citeste de la tastatura pretul cosului de cumparaturi. Afiseaza pretul cu un discount de 25%.
"""

"""
7. Se da string-ul: zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'.
Transforma string-ul in lista, folosindu-te de o metoda ajutatoare de pe string.
"""

# zile_saptamana = 'luni, marti, miercuri, joi, vineri'
# lista1 = list[zile_saptamana]
# print(lista1)

"""
8. Scrie un program care solicita utilizatorului sa introduca varsta sa
și returneaza un mesaj personalizat, in funcție de varsta introdusa.
Daca varsta este mai mare sau egala cu 18, programul trebuie sa afiseze
mesajul "Esti major si poti vota".
In caz contrar, programul trebuie sa afiseze mesajul "Esti minor si nu poti vota inca".
"""
# varsta = int(input('introdu varsta '))
# if varsta <=0:
#     print(f'Introdu o varsta valida')
# elif varsta < 18:
#     print(f'Esti minor')
# else:
#     print(f'Esti major!')
"""
9. Scrie un program care primeste un pret de la tastatura si afiseaza
un mesaj daca prețul este mai mare sau mai mic decât 100 de lei.
"""
# pret = int(input(f' INTRODU UN PRET'))
# if pret > 100:
#     print('pretul este mai mare de 100 de lei')
# elif pret < 100:
#     print('pretul este mai mic de 100 de lei')
"""
10. Citeste doua numere intregi de la tastatura. Printeaza produsul dintre cele doua numere
daca acesta este mai mic sau egal decat 1000, altfel printeaza suma lor.
"""

# a = int(input('introdu un numar intreg '))
# b = int(input('introdu un numar intreg '))
# c = a * b
# d = a + b
# if c <= 1000:
#     print(c)
# else:
#     print(d)

"""
11. Se dau doua liste:
lista_1 = [10, 20, 30, 40, 50, 10]
lista_2 = [1, 2, 3, 4, 5]
Pentru fiecare lista verifica daca primul si ultimul element sunt egale.
In functie de rezultat, afiseaza un mesaj.
"""
# lista_1 = [10, 20, 30, 40, 50, 10]
# lista_2 = [1, 2, 3, 4, 5]
# if lista_1[-1]==lista_2[-1] and lista_1[0]==lista_2[0]:
#     print('primul si ultimul element sunt egale')
# else:
#     print('Nu sunt egale elementele')


"""
12. Scrie un program care afiseaza de cate ori apare litera 'e' in
stringul str_1 = 'Emma is a sofware developer.'
"""

str_1 = 'Emma is a sofware developer.'
print(str_1.count('e'))


"""
13. Scrie un program in care citesti de la tastatura doua nr intregi,
numite base si exponent.
Afiseaza intr-un mesaj sugestiv, valoarea lui base la puterea exponent.
Atentie: indiferent daca utilizatorul a introdus un numar pozitiv 
sau negativ
ca si exponent, trebuie sa ridici base la puterea exponent pozitiv.
hint: exploreaza functia abs() si vezi cum o poti folosi
"""


"""
14. Scrie un program in care se citeste de la tastatura un string.
Daca string-ul are numar impar de caractere, afiseaza un string care
contine primul caracter, caracterul din mijloc si ultimul caracter
al string-ului citit de la tastatura.
Daca string-ul are numar par de caractere, afiseaza un string care 
contine doar primul
si ultimul caracter  al string-ului citit de la tastatura.
"""

# cuvant = input('Introdu un cuvant ')
# if len(cuvant) % 2 == 0:
#     print('Cuvantul are un numar  par de caractere')
# else:
#     print('Cuvantul are un numar impar de caractere')


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
str1 = 'Abc'
str2 = 'Xyz'
str3 = str1[0].lower() + str2[0].upper() + str1[1].upper() + \
       str2[1].upper() + str1[2].upper() + str2[2].lower()
print(str3)


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
h. Foloseste slicing pe lista, astfel incat sa obtii o lista cu al doilea, 
al treilea si al patrulea element.
"""

fruits = ["apple", "banana", "cherry"]
# a
fruits[0] = 'kiwi'
print(fruits)
# b
fruits.append('oranges')
print(fruits)
# c
fruits.insert(1, 'lemon')
print(fruits)
# d
fruits.remove('banana')
print(fruits)
# e
print(fruits[-1])
# f
print(fruits[-2])
# g
print(len(fruits))
# h   nu stiu


"""
17. Inverseaza lista my_list = [100, 200, 300, 400].
"""
# my_list = [100, 200, 300, 400]
# print(my_list[::-1])

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
cumparaturi = 'rosii,crastaveti,branza,oua'
print(type(cumparaturi))
# list_cumparaturi = lst(cumparaturi)
# print(list_cumparaturi)
# a
lista = list[cumparaturi]
print(lista)
# b
sorted_list = sorted(lista)    # nu stiu
print(sorted_list)
# c
sorted_list.insert(2, 'cartofi')
print(sorted_list)
sorted_list.remove('cartofi')
print(sorted_list)
"""
19. Se da lista fructe = ['capsuni', 'mere', 'lamai'].
Converteste lista la string si afiseaza string-ul. A se vedea metoda join(). (search on google)
"""
fructe = ['capsuni', 'mere', 'lamai']
# nu stiu

"""
20. Se da lista numere = [1, 2, 3, 4, 56, 22, 5].
Afiseaza elementul cu valoarea maxima din string. (google- functia max())
"""
# numere = [1, 2, 3, 4, 56, 22, 5]
# nr_maxim = max(numere)
# print(nr_maxim)
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
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# print(sample_dict["city"])
# sample_dict["salary"] = 10000
# print(sample_dict)
# sample_dict.pop('age')
# print(sample_dict)
# sample_dict.update({"employment_date": '12.12.2020'})
# print(sample_dict)
# print(sample_dict.get('country', 'Dicionarul nu detine cheia'))
# sample_dict.update({'country': 'Romania'})
# print(sample_dict)
"""
23. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza toate cheile din dictionar. (HINT: metoda keys())
b. Afiseaza toate valorile din dictionar. (HINT: metoda values())
c. Verifica lungimea dictionarului.
"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# print(sample_dict.keys())
# print(sample_dict.values())
# print(len(sample_dict))
# print(sample_dict.get('birth', 'nu este'))
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
# keys = input('INTRODU CHEIA CAUTATA: ')
# print(persoana[keys])
# print(persoana.get(keys, 'nu este'))


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

persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
cheia = input('introdu cheia de adaugat in dictionar ')
valoarea = input('introdu valoarea de adaugat in dictionar ')

persoana.update({cheia: valoarea})
print(persoana)  # -> {'nume': 'Alex', 'varsta': 25, 'oras': 'Bucuresti',
# 'masina': 'true'}


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
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}

"""
27. Concatenarea a doua dictionare.
Se dau doua dictioanare:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
Sa se concateneze cele doua dictionare folosind metoda update().
Observatie: Metoda update() o putem folosi pentru a adauga unul sau mai multe
perechi cheie:valoare in dictionar.
"""

"""
28. Se da urmatoarea lista cu dictionare:
lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
a. Adauga perechea {'c':'3'} in primul dictionar din lista.
b. Adauga un nou dictionar ca element in lista. Adauga-l la final.
c. Aduaga un nou dictionar ca element in lista, la indexul 1.
d. Verifica daca in al doilea dictionar din lista se gaseste cheia 'c'.
"""

"""
29.
Se citeste de la tastatura un numar.
a. Printeaza un mesaj sugestiv daca numarul este par sau nu.
b. Daca numarul este multiplu de 4, afiseaza un mesaj sugestiv.
"""

"""
30.
Se citesc de la tastatura doua numere, num si check. Verifica daca
num este divizibil cu check si afiseaza un mesaj corespunzator catre 
utilizator.
"""
num = int(input('Introdu un numar pentru verificare '))
check = int(input('Introdu un numar divizor '))

if num % check:
    result = num % check
    print(result, 'este divizibil')
else:
    print('nu este')


"""
31. Se da dictionarul:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a. Foloseste metoda get() pentru a printa valoarea cheii 'model'.
b. Schimba valoarea cheii 'year' in 1970.
c. Adauga perechea cheie:valoare 'color':'red' in dictionar.
Adaug-o folosind accesarea dictionarului prin cheie (car['color']) si 
dand o valoare.
Adaug-o folosind metoda update()
d. Foloseste metoda pop() pentru a sterge 'model' din dictionar.
e. Foloseste metoda empty() pentru a 'goli' dictionarul.
"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
    }
# a
print(car.get('model'))
# b
car['year'] = 1970
print(car)
# c
(car['color']) = 'red'
print(car)
# d
car.pop('model')
print(car)
# e
car.clear()       # -> {}   clear e functie care goleste dictionarul
print(car)
