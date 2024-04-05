# Interactiunea cu fisiere text

"""
open() = functie folosita pentru a interactiona cu un fisier
in Python
- ne returneaza o referinta catre fisierul cu care dorim sa
interactionam (practic, este fisierul deschis)

Functia open() poate sa ia mai multi parametri:

1. un parametru OBLIGATORIU, numit file
- calea catre fisierul cu care dorim sa interactionam/ file path
- file path = locatia unde se afla fisierul nostru relativ
cu programul nostru
- Un file path este compus din 3 mari parti:
    -- folder path = calea catre folder-ul in care avem localizat fisierul
    -- file name = numele fisierului
    -- file extension = extensia fisierului (.txt, .csv, .json etc)

2. parametru optional -> parametrul mode:
- modul in care dorim sa interactionam cu fisierul
- este un string si poate sa aiba mai multe valori
- cele mai comune valori pentru parametrul mode:
    -- 'r' -> deschidem fisierul pentru a citi informatii din el
    -- 'w' -> deschidem fisierul pentru a scrie informatii in el
! ATENTIE - daca in fisier aveam deja informatii, acestea sunt SUPRASCRISE
    -- 'a' -> deschidem fisierul pentru a scrie informatii la finalul acestuia/
    il extindem/il actualizam
"""

# deschid fisierul dummy.txt in modul read (citesc informatii din el)
fisier = open(file="dummy.txt", mode="r")

# metoda readlines() -> citesc tot continutul fisierului
# se returneaza o lista in care fiecare element este
# o linie din fisier
lines = fisier.readlines()
print(lines)
print(lines[0])

# deschidem fisierul dogs.txt in modul read (citim informatii din el)
fisier1 = open(file="fisiere_text/dogs.txt", mode="r")
# lines1 = fisier1.readlines()
# print(lines1)
print(fisier1.read())

# dupa ce interactionam cu un fisier, acesta trebuie inchis
# de ce?'
# pentru ca vor ramane datele din fisier vulnerabile/usor
# accesibile de catre oricine
# + scade eficienta programului/aplicatiei noastre
# pentru ca orice fisier deschis este o resursa care ocupa
# memorie
fisier.close()
fisier1.close()

# => with statement este o abordare mai buna/ abordarea preferata
# de interactiune cu fisierele pentru ca partea de curatare/clean up/
# inchidere fisier are loc automat pentru noi
with open(file="dummy.txt", mode="r") as f:
    lines = f.readlines()
    print(lines)


def citire_din_fisier_txt(calea_catre_fisier_txt):
    with open(calea_catre_fisier_txt, 'r') as file:
        return file.readlines()


print(citire_din_fisier_txt("dummy.txt"))
print(citire_din_fisier_txt("fisiere_text/dogs.txt"))

with open(file="dummy.txt", mode="r") as f:
    print(f.readline())   # imi da prima linie
    print(f.readlines())  # imi da restul liniilor sub forma de lista
    # print(f.readline())
    # f.writelines(["ceva"]) # eroare -> fisierul a fost deschis in modul read/citire ->
    # -> nu putem sa facem operatii de scriere in fisier

# scrierea in fisiere text
# -> modul "w" sau "a", in functie de necesitati

# scriem informatii intr-un fisier nou
# (il si cream in acelasi timp)
# folosind modul "w"
with open("dummy2.txt", mode="w") as file:
    file.write("Continut nou")

# suprascriem continutul dintr-un fisier existent
# folosind tot modul "w"
with open("dummy2.txt", mode="w") as file:
    file.write("Continut suprascris")

with open("dummy2.txt", mode="w") as file:
    file.writelines([
        "This is the first line\n",
        "This is the second line\n"
    ])

# extindem/actualizam continutul unui fisier text
# folosind modul "a"
with open("dummy2.txt", mode="a") as file:
    file.writelines([
        "This is the third line\n",
        "This is the fourth line\n"
    ])

