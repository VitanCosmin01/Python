# factory = TranslatorFactory()
#
# english_trans = factory.get_translator('en')
# spanish_trans = factory.get_translator('es')
#
# print(f'In engleza zicem {english_trans.localize("masina")}')
# print(f'In spaniola zicem {spanish_trans.localize("masina")}')
#
# def Factory(cls,):
'''
Factory Pattern
Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica). Fabrica are posibilitatea de a crea obiecte din mai multe clase (de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).


Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare, ne va da traducerea lui în acea limba (exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa) numita get_translator(language) – in functie de parametrul language, returnează un translator object.

'''
class FrenchLocalizer:

    def __init__(self):
        self.translations = {
           "car": "voiture",
           "bike": "bicyclette",
           "cycle": "cyclette"
       }

    def localize(self, msg):

        return self.translations.get(msg, msg)


class SpanishLocalizer:

    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }

    def localize(self, msg):

        return self.translations.get(msg, msg)


class EnglishLocalizer:

    def localize(self, msgy):
        return msgy


def factory(language = "English"):

    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()


if __name__ == "__main__":

    f = factory("French")
    e = factory("English")
    s = factory("Spanish")

message = ["car", "bike", "cycle"]

for msg in message:
    if f and e and s:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))