# """
#
# Pachete python. Interacțiune cu fișiere.
#
# 1. Create a text file called “hello.txt” and add the following text inside of it:
# Python
# Java
# Javascript
# C/C++/C#
# PHP
# Node.js
#
# Write a short program to read and display the text file
# """
#
def citire_hello(cale_fisier):
    fisier = open(file=cale_fisier, mode='r')
    lines = fisier.read()
    print(lines)
    fisier.close()
#
# citire_hello('Hello.txt')
# ############
# # def citire_Hello(D:\Curs PYTA5\de jucat\workshop_17.07\Hello.txt):
# #     with open(workshop_17, 'r')as file:
# #         return file.readlines()
#
# ##############
# # Rezolvare ex 1:
#
#
# with open(file="hello.txt", mode="w") as file:
#     file.writelines([
#         "Python\n"
#         "Java\n"
#         "Javascript\n"
#         "C/C++/C#\n"
#         "PHP\n"
#         "Node.js\n"
#     ]
#     )
#
#
# def read_file(file_path):
#     with open(file_path, "r") as f:
#         return f.readlines()
#
# print(read_file(file_path="hello.txt"))
#
#
#
#
#
#
# """
# 2. Write a short program to append the following lines to “hello.txt” (you will use a list of
# strings and a for-loop):
# Go
# Kotlin
# Swift
#
# Display the new contents of the file.
# """
# # Rezolvare ex 2:
#
#
#
# f = open("hello.txt", "a")
# f.write("Go\n"
#         "Kotlin\n"
#         "Swift\n"
#         )
# f.close()
#
# f = open("hello.txt", "r")
# for x in f:
#     print(x)
# """
# 3. Write a short program that reads the “hello.txt” file and displays every other line
# (only odd lines).
# """
# # Rezolvare ex 3:
#
#
#
# with open("hello.txt", "r") as f:
#     lines = f.readlines()
#     # for index, line in enumerate(lines):
#     #     if (index + 1) % 2 == 0:
#     #         print(line)
#     for index in range(1, len(lines), 2):
#         print(lines[index])
# """
# 4. Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`.
# Each file will contain the sentences below:
#
# My name is letter X.
# I am the 24th letter of the alphabet.
#
# Make sure you use the correct ending for the letter’s number
# (e.g. 1st, 2nd, 3rd, etc.)
# """
#
#
#
# #   din libraria string, putem sa ne folodim de variabila ascii.uppercase
# #  pentru a avea acces la toate literele din alfabet scrise cu majuscula
# #  ascii.upercase este un string
#
# import string
#
# letters = string.ascii_uppercase
# print(letters)
#
# for letter in letters:
#     print(type(letter))
#
#
#
# for index in range(0, len(letters)):
#     print(letters[index])
#     file_name = f'{letters[index]}.txt'
#
#     print(file_name)
#     if index == 0 or index == 20:
#         position = f'{index+1}st'
#     elif index == 1 or index == 21:
#         position = f'{index+1}nd'
#     elif index == 2 or index == 22:
#         position = f'{index+1}rd'
#     else:
#         position = f'{index+1}th'
#     with open(file_name, 'w') as file:
#         file.write(f'My name is letter {letters[index]}\n')
#         file.write(f'I am the {position} letter of the alphabet.\n')
# ########## o varianta de a afla pozitia fiecarei litere in alfabet
# # metoda ord arata un cod asociat fiecarei litere
# import string
#
# letters = string.ascii_uppercase
# print(letters)
#
# for letter in letters:
#     print(letter)
#     print(ord(letter))
#     index = ord(letter) - ord('A')
#     # litera B: 66 - 65 = 1
#     # litera C: 67 - 65 = 2
# """
# 5. Create a csv file called “students.csv” and add the following text inside of it:
# id,fname,lname,age,grade
# 1,Maria,Popescu,31,7.5
# 2,Andrei,Ionescu,26,8.0
# 3,Adriana,Marinescu,21,7.5
# 4,Matei,Gheorghescu,42,8.5
# 5,Eusebiu,Pop,33,9.5
# 6,Ioana,Popa,29,9.0
#
# Read the file using Python’s `csv` standard library, and display it
# in the terminal as a table, using the options for string formatting from Python:
#
#
# id	fname		lname		age	grade
# ---------------------------------------------------
# 1	Maria		Popescu		31	7.5
# 2	Andrei		Ionescu		26	8.0
# 3	Adriana		Marinescu		21	7.5
# 4	Matei		Gheorghescu	42	8.5
# 5	Eusebiu		Pop			33	9.5
# 6	Ioana		Popa			29	9.0
# """
# import csv
#
# # with open('students.csv', mode= 'w', newline='') as f:
# #     writer = csv.writer(f)
# #     writer.writerow(["id", "fname", "lname", "age", "grade"])
# #     writer.writerow([1, 'Maria', 'Popescu', 31, 7.5])
# #     writer.writerow([2, 'Andrei', 'Ionescu', 26, 8.0])
# #     writer.writerow([3, 'Adriana', 'Marinescu', 21, 7.5])
# #     writer.writerow([4, 'Matei', 'Gheorghescu', 42, 8.5])
# #
#
# with open('students.csv', mode='r') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     print(f'{header[0]:<4} {header[1]:<10} {header[2]:<10} {header[3]:<4} {header[4]:<4} ')
#     print('-'*40)
#
#
#     for row in reader:
#         print(f'{row[0]:<4} {row[1]:<10} {row[2]:<10} {row[3]:<4} {row[4]:<4}')

###################### varianta din clasa


import csv

with open("students.csv", mode="w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'fname', 'lname', 'age', 'grade'])
    writer.writerow([1, 'Maria', 'Popescu', 31, 7.5])
    writer.writerow([2, 'Andrei', 'Ionescu', 26, 8.0])
    writer.writerow([3, 'Adriana', 'Marinescu', 21, 7.5])
    writer.writerow([4, 'Matei', 'Gheorghescu', 42, 8.5])
    writer.writerow([5, 'Eusebiu', 'Pop', 33, 9.5])
    writer.writerow([6, 'Ioana', 'Popa', 29, 9.0])

with open("students.csv", mode='r') as f:
    reader = csv.reader(f)
    header = next(reader)

    print(f'{header[0]:<4} {header[1]:<10} {header[2]:<13} {header[3]:<5}  {header[4]:<7}')
    print('-'*43)
    for row in reader:
        print(f'{row[0]:<4} {row[1]:<10} {row[2]:<13} {row[3]:<5}  {row[4]:<7}')
####################
"""
6. Read again the information from the csv file above, store it all in a list of data, and then 
write a new file,
called “students.json”, which will contain a valid JSON object. 

Use the following format for each student (and use Python’s standard JSON module):
[
    {
        "id": 1,
        "fname": "Maria",
        "lname": "Popescu",
        "age": 31,
        "grade": 7.5
    },
    ...
]
"""
import csv, json

# csv.DictReader(f)

my_list = []
with open('students.csv', mode='r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(reader)
        my_list.append(row)
print(my_list)
with open("students.json", mode='w') as f:
    json.dump(my_list, f, indent=4)


"""
7.
Create a new PyCharm project. Make sure it has a virtualenv. Install all the 
following packages from PYPI:
behave
behave-html-formatter
requests
selenium
webdriver-manager
Use pip to create a `requirements.txt` file. Send your project to a colleague and 
ask them to install all 
dependencies using pip.
"""