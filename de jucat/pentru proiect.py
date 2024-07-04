class Carte:

    def __init__(self, pagini):
        self.__pagini = pagini

    @property
    def pagini(self):
        print("Accesare numar pagini")
        return self.__pagini

    @pagini.setter
    def pagini(self, pagini):
        if pagini < 1000:
            print("Setare numar pagini")
            self.__pagini = pagini

    @pagini.deleter
    def pagini(self):
        print("Stergere atribut cu numar pagini")
        self.__pagini = None


carte1 = Carte(4)
carte1.pagini = 100  # Setare numar pagini
print(carte1.pagini)  # Accesare numar pagini / 100
del carte1.pagini  # Stergere atribut cu numar pagini
print(carte1._Carte__pagini)  # None
del carte1._Carte__pagini
# print(carte1._Carte__pagini)  # AttributeError: 'Carte' object has no attribute '_Carte__pagini'