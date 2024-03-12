"""

OOP - advance

Exerciții - studiu în workshopul de weekend

1. ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
"""
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")


"""
2. INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
"""


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        pass

    @property
    def latura(self):
        print("getter")
        return self.__latura

    @latura.setter
    def latura(self, latura_noua):
        print("setter")
        self.__latura = latura_noua

    @latura.deleter
    def latura(self):
        print("am sters latura")
        self.__latura = 0


"""
3. Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit 
din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

POLYMORPHISM 
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
"""


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        pass

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza cercului este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza_noua):
        print(f'Setter: Raza noua este {raza_noua}')
        self.__raza = raza_noua

    @raza.deleter
    def raza(self):
        print('Deleter: Am sters valoarea razei')
        self.__raza = 0


"""
4. Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""


patrat1 = Patrat(5)                # instantiat un obiect si setat o valoare pentru latura
print(patrat1.latura)              # accesat latura pe obiect

patrat1.latura = 8                  # setter
print(patrat1.latura)

del patrat1.latura                  # deleter
print(patrat1.latura)

cerc1 = Cerc(9)
print(cerc1.raza)


