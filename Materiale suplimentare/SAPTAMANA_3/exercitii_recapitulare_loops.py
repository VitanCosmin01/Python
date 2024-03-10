"""
1. Scrie un program care afiseaza primii 7 multiplii
a lui 7.

HINT: for loop + if + break
Expected Output: 0 7 14 21 28 35 42 49
"""
# # varianta 1
# result = ('')
# for numar in range(0, 8):
#     x = 7 * numar
#     result += str(x)
#     result += ' '
#
# print(result)
# # varianta 2
# resl = ''
# y = 0
# for i in range(1, 1000):
#     if y == 7:
#         break
#     if i % 7 == 0:
#         resl += str(i) + ' '
#         y += 1
#
# print(resl)

"""
2. Scrie o functie care adauga patratul fiecarui numar
intr-o noua lista si afiseaz-o.

Aceasta functie va primi ca parametru o lista.

Example input: [2, 3, 4]
Expected output: [4, 9, 16]
"""
# i = [2, 3, 4]
# for i in range(10):
#     i += i**2
#     print(i, end=',')



"""
3. Scrie o functie care primeste ca parametru o lista
de numere intregi.

Separa numerele pozitive de cele negative si returneaza-le.

Apeleaza functia cu diferite argumente si afiseaza rezultatul
conform exemplului de mai jos:

Example input: [1, 2, 5, -2, 3, -5]
Expected output:
Positive: [1, 2, 5, 3]
Negative: [-2, -5]
"""
lista = [1, 2, 5, -2, 3, -5]
positive = []
negative = []
for a in lista:
    if a > 0:
        positive.append(a)
    else:
        negative.append(a)

print("Positive: ", positive)
print("Negative: ", negative)


"""
4. Scrie o functie care calculeaza factorialul unui numar natural
pozitiv luat ca si parametru si returneaza rezultatul.

Example input: 6
Expected output: 720
"""

# name1 = 'Dholi'
# print(name1[:3]) #=> Dho
# name2 = 'Kohli'
# print(name2[1:]) #=> ohli
# result =name1[:3] + name2[1:]
# print(result) #=> Dhoohli

# Exemplul 3 - Cautarea unui element intr-o lista
# numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
#
# search_value = int(input("Ce numar cautati? "))
#
# index = 0
# while index < len(numbers):
#     if numbers[index] == search_value:
#         print(f"Valoarea a fost gasita la indexul: {index}")
#         break
#     index += 1
# else:
#     print("Valoarea nu a fost gasita in lista!")