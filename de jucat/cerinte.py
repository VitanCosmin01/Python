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
       pass


    def inmatriculare(self, nr_inmatriculare):
        pass


    def vopseste(self, culoare):
        pass


    def accelereaza(self, viteza):
        pass

    
    def franeaza(self):
        pass


masina1 = Masina('1300', 100)




