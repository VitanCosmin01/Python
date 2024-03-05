"""
Mașină
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori disponibile (set), înmatriculată (bool)
   Culoare = gri - toate mașinile când ies din fabrică sunt gri
   Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
   Culori disponibile = alege tu 5-7 culori
   Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
   Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
descrie() - se vor printa toate atributele, în afară de culori_disponibile
înmatriculare() - va schimba atributul înmatriculată în True, si se va da un numar de inmatriculare
vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile,
    altfel afișați o eroare
accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare,
    dacă viteza e mai mare decât viteza_max - masina va accelera până la viteza maximă
franeaza() - mașina se va opri și va avea viteza 0
"""
from abc import ABC, abstractmethod

class IMasina(ABC):

    @abstractmethod
    def descrie(self):
        pass

    @abstractmethod
    def inmatriculare(self, nr_inmatriculare):
        pass

    @abstractmethod
    def vopseste(self, culoare):
        pass

    @abstractmethod
    def accelereaza(self, viteza):
        pass

    @abstractmethod
    def franeaza(self):
        pass


class Masina(IMasina):
    MARCA = 'Dacia' #daca scriem o variabila cu litere mari => nu se va mai schimba
    CULORI_DISPONIBILE = {'negru', 'rosu', 'verde', 'galben', 'albastru'}

    # def __init__(self,  model, viteza_maxima, viteza_actuala = 0, culoare = 'gri', inmatriculata = False, nr_inmatriculare = None):
    #     self.model = model
    #     self.viteza_actuala = viteza_actuala
    #     self.__culoare = culoare
    #     self.viteza_maxima = viteza_maxima
    #     self.__inmatriculata = inmatriculata
    #     self.__nr_inmatriculare = nr_inmatriculare

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_actuala = 0
        self.__culoare = 'gri'
        self.viteza_maxima = viteza_maxima
        self.__inmatriculata = False
        self.__nr_inmatriculare = None



    def descrie(self):
        print(f"Marca: {self.MARCA}, Modelul: {self.model}, V. Maxima: {self.viteza_maxima}")
        print(f"V. Actuala: {self.viteza_actuala}, Culoarea: {self.culoare}")
        print(f"Inmatriculata?: {self.inmatriculata}, Nr Imatriculare?: {self.nr_inmatriculare}")

    def inmatriculare(self, nr_inmatriculare):
        self.__nr_inmatriculare = nr_inmatriculare
        self.__inmatriculata = True


    def vopseste(self, culoare):
        if culoare in self.CULORI_DISPONIBILE:
            self.__culoare = culoare
        else:
            print("Culoarea NU este dipsonibila")

    def accelereaza(self, viteza):
        if viteza < 0:
            print("VIteza nu poate sa fie o valoare NEGATIVA")
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        self.viteza_actuala = 0

    @property
    def culoare(self):
        print("Getter culoare")
        return self.__culoare

    @property
    def inmatriculata(self):
        print("Getter inmatriculata")
        return self.__inmatriculata

    @property
    def nr_inmatriculare(self):
        print("Geter nr_inmatriculare")
        return self.__nr_inmatriculare


masina1 = Masina("1300", 100)
masina1.descrie()
masina1.inmatriculare("SB-93-STF")
masina1.descrie()
masina1.vopseste("Rosu")
masina1.descrie()
print(masina1.culoare)

print(masina1.viteza_actuala)
masina1.accelereaza(-1)
print(masina1.viteza_actuala)
masina1.accelereaza(200)
print(masina1.viteza_actuala)
masina1.accelereaza(50)
print(masina1.viteza_actuala)
masina1.franeaza()
print(masina1.viteza_actuala)

