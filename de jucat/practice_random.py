import random

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Initial: ', lista)
random.shuffle(lista)
print('Dupa amestecare: ', lista)

##################################
# numere întregi cu semn
for x in range(5):
    print(random.randint(-100,100))
# alegem aleator elemente din listă
vocale = ['a', 'e', 'i', 'o', 'u']
for x in range(3):
    print(random.choice(vocale))

##################################

# în intervalul [0.0, 1.0)
for x in range(5):
    print(random.random())
# între 0 și 100
for x in range(5):
    print(round(random.random()*100))
# între 0 și 10000
for x in range(5):
    print(round(random.random()*10000))

############################
# Folosim seed() pentru a tipări cinci numere aleatoare, iar ca parametru vom specifica, să spunem, 17:
random.seed(17)
for x in range(5):
    print(random.randint(1, 10))

###############################
# Ghiceste numarul
numar = random.randint(1, 10)
ghicit = int(input("n="))
while numar != ghicit:
    if ghicit > numar:
        print("Este mai mic!")
    else:
        print("Este mai mare!")
    ghicit = int(input("n="))
print("Felicitari, ai ghicit numarul", ghicit, "!")