"""
Context Managers
Se da un fisier text hello.txt, care contine un text scurt.
Deschideți fișierul și citiți conținutul, folosind urmatoarele 2 metode:
try - finally
Fișierul se deschide înainte de try, folosind functia open
În interiorul try citim conținutul folosind functia read
În finally se închide fișierul
with (context manager)
Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul,
pentru ca context managerul face asta pentru noi.
"""

f = open("hello.txt", "w")
txt = f.writelines("Hello Python! I am here to learn more about you!")
f.close()

f = open("hello.txt", "r")
try:
    txt = f.read()
    print(txt)
finally:
    f.close()




