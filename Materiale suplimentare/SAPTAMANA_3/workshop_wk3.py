

# 1.Funcție care să calculeze și să returneze suma a două numere


# def sum(a,b):
#
#     return a+b
#
# print(sum(5,8))


#2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
# def parity





#3. Funcție care returnează numărul total de caractere din numele tău complet.
#(nume, prenume, nume_mijlociu)

# def nume(nume, prenume, nume_milociu = ''):
#     return len(nume+prenume+nume_milociu)
#
# print(f'Lungimea numelui complet este {nume("Laurentia", "Vasilasco")}.')


# varianta 2
# def nume(nume, prenume, nume_milociu = ''):
#     if type(nume)==str and type(prenume)==str and type(nume_mijlociu)==str:
#         return len(nume+prenume+nume_milociu)
#     return -1
#
# print(f'Lungimea numelui complet este {nume("Laurentia", "Vasilasco")}')
# if nume(10, 20, 30)>0:
#     print(f'Lungimea numelui complet este {nume("Laurentia", "Vasilasco")
# else:
#     print('Introduceti parametri')
#

#    .....................

# 4. Funcție care returnează aria dreptunghiului

#
# def aria(a, b):
#      return a * b
#
# print(f'Aria este {aria(10, 20)}')





# 5. Funcție care returnează aria cercului

# def circlearia(pi, radius):
#      return pi * radius ** 2:
#
# print(f'Aria cercului este {circlearia(3.14. 20)}')


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
#
# def cara(x, y):
# z = 0
#     for i in range(len(y)):
#         if x == y[i]:
#             z += 1
#         if z > 0:
#         return True
#     else:
#         return False

# 13. Funcție care primește o listă de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def item_count(my_list):
    dicti = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0
    }
    for item in dicti.keys():
        dicti[item] = my_list.count(int(item))

    return dicti

print(item_count([1, 3, 1, 5, 9, 7, 7, 5, 5]))


# 2. Clasa Dreptunghi
#      Atribute: lungime, lățime, culoare
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# aria()
# perimetrul()
# schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
# Poți verifica schimbarea culorii prin apelarea metodei descrie().

# class Dreptunghi:
#     lungime = 39
#     latime = 54
#     culoare = 'blue'
#
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descriere(self):
#         print(f'Acest dreptunghi are o lungime de {self.lungime} si o latime de {self.latime}.
#         Culoarea lui este {self.culoare}.')
#
#     def area(self):
#         return self.lungime * self.latime
#
#     def perimetru(self):
#         return 2 * (self.lungime + self.latime)
#
#     def change_color(self, new_color):
#         self.culoare = new_color
#
#
# dreptunghi = Dreptunghi(39, 54, 'blue')
# dreptunghi.change_color('green')
# print(f'Aria dreptunghiului este {dreptunghi.area()}.')
# dreptunghi.descriere()
# print(f'Perimetrul este {dreptunghi.perimetru()}.')

# descriere_masina = "masina asta costa 20000 de euro."
# print(descriere_masina.upper())
#
# mystr_1 = "minge"
# mystr_2 = "rosie"
#
# result_1 = mystr_1 + mystr_2
# print(result_1)
#
# result_2 = f'{mystr_1} {mystr_2}'
# print(result_2)
