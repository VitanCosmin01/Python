# EXERCITII BONUS FISIERE

"""
EX1:
1. Copierea continutului dintr-un fisier in alt fisier.
- creeaza un fisier sursa.txt (din cod) si pune continut in el
(continutul e la alegerea ta)
- copiaza continutul din fisierul sursa.txt intr-un fisier nou,
numit destinatie.txt.
Afiseaza apoi contintul din fisierul destinatie.txt
"""
# file1 = open("sursa.txt", "w")
# file1.write("This is my first tryout!\n"
#             "And i am experimenting the new line!\n")
# print(file1)
# file1.close()
# file1 = open("sursa.txt", "a")
# file1.write("Text adaugat dupa inchidere")
# print(file1)

# Creează fișierul sursa.txt și adaugă conținut
with open("sursa.txt", "w") as sursa_file:
    sursa_file.write("Acesta este fisierul, fisierul, fisierul sursa din care se va "
                     "copia textul in cel destinatie")

# Copiaza continutul din sursa in destinatie
with open('sursa.txt', 'r') as sursa_file, open('destinatie.txt', 'w') as destinatie_file:
    for line in sursa_file:
        destinatie_file.write(line)

# Afișează conținutul din destinatie.txt
with open('destinatie.txt', 'r') as destinatie_file:
    print("Conținutul din fișierul destinatie.txt:")
    print(destinatie_file.read())


"""
EX2: Numararea cuvintelor
- creeaza o functie care sa ia ca si parametru un cuvant si un fisier txt,
si afiseaza de cate ori apare acel cuvant in fisierul text.
"""


def counting_words(word, file):
    try:
        with open(file, "r") as file:
            content = file.read()
            word_count = content.lower().count(word.lower())
        return word_count
    except FileNotFoundError:
        print(f'File {file} not found!')
        return 0


# Example usage
counting_words("fisierul", "sursa.txt")

"""
EX3: Creeaza un fisier CSV, numit produse.csv cu urmatorul continut:
- coloane: id, nume_produs, pret, cantitate.
Adauga 4 randuri in fisierul csv cu detalii despre 4 produse.

Citeste informatiile din fisierul csv folosind DictReader si
pune informatiile citite intr-un fisier json, numit "produse.json".
"""