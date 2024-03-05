import random
k = 0
ok = 0
nivel = 0
judete = ['BUCURESTI', 'DAMBOVITA', 'MARAMURES', 'VASLUI', 'TULCEA', 'TELEORMAN', 'ARGES', 'HUNEDOARA', 'IALOMITA', 'CALARASI', 'CONSTANTA', 'SUCEAVA', 'BOTOSANI', 'IASI', 'VRANCEA']

print('''Acest joc se numeste SPANZURATOAREA
Nivele de dificultate:
1. Usor  - 10 incercari nereusite
2. Mediu -  7 incercari nereusite
3. Greu  -  4 incercari nereusite''')

while nivel not in ['1','2','3']:
    print("Alegeti nivelul de dificultate:",end=" ")
    nivel = input()
    if nivel == '1': incercari=10
    if nivel == '2': incercari=7
    if nivel == '3': incercari=4
s=random.choice(judete)
print("Cuvantul dumneavoastra: ", end="")
for i in s:
    print('_ ', end="")
print()
print("INTRODUCETI LITERE MARI!")
gasite = []
incercate = []
while k < incercari and ok == 0:
    #print("Litere ghicite:",end="")
    #print(gasite)
    print("Litere incercate:",end=" ")
    for i in incercate:
        print(i,end=" ")
    print()
    print('Introduceti o litera: ',end="")
    l = input()
    incercate.insert(len(incercate), l)
    if l in s:        
        gasite.insert(len(gasite), l)
        print("Corect!!!")
        print("Cuvantul dumneavoastra: ", end = "")
        for i in s:
            if(i in gasite):
                print(i, " ", end = "")
            else:
                print('_ ', end = "")
    else:
        k = k + 1
        print("Gresit! Mai aveti ", incercari-k, " incercari!!!", end="")
    if l in s:
        p = 0
        for i in s:
            if not(i in gasite):
                p = p + 1
        if p == 0:
            ok = 1
    print()
    print()
if k == incercari:
    print("Ati pierdut!!!")
else:
    print("Ati castigat!!!")
print("Cuvantul este: ", s.upper())

