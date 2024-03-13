"""Imagine
you're a teacher with a set of final grades for your class. You want to see how
many students scored above 8.0 to assess overall class performance.

Task

Given the list of grades, calculate the number of grades that are above 8.0
"""

grades = [8.5, 7.9, 6.8, 8.2, 9, 6.3, 8.4]
count = 0
lista = []
# Count the number of grades above 8.0
for i in grades:
    if i >= 8:
        count += 1
        lista.append(i)

# Display the result
print(count)     # afiseaza numarul de note mai mari decat 8
print(lista)      # afiseaza o lista cu toate notele mai mari decat 8


prices = [10, 54, 9, 44, 6, 26, 15]
total = 0
for price in prices:
    total += price        # total = total + price
    print(total)
    if total > 100:
        print("Limit exceeded")
        break

while True:
    text = input()
    print(text)
    if text == "Stop":
        break
