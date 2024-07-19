"""
1. Implementeaza o clasa Employee.
Atribute:
- id
- name
- salary
- department

Metode:
- assign_department - schimba departamentul angajatului.
- print_employee_details - afiseaza detaliile despre angajat
- calculate_salary - calculeaza salariul angajatului.
Aceasta metoda ia doua argumente: salary si hours_worked.
Daca angajatul a lucrat mai mult de 50 de ore, atunci la salariu
se va adauga plata pe overtime, aceasta fiind orele extra * salariu/50.

Exemple date angajati:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
"""


class Employee:
    def __init__(self, id_no, name, salary, department):
        self.id_no = id_no
        self.name = name
        self._salary = salary
        self.department = department

    def __str__(self):
        return f'{self.id_no}, {self.name}, {self._salary}, {self.department}!'

    def assign_department(self, new_department):
        self.department = new_department
        return f'The new department is: {self.department}!'

    def employee_details(self):
        return f'Details for are: \nID: {self.id_no}, Name: {self.name}, Salary: {self._salary}, Department: {self.department}'

    def calculate_salary(self, salary, hours_worked):
        if hours_worked > 50:
            extra = hours_worked - 50
            self._salary = self._salary + extra * salary/50
            return self._salary


employee1 = Employee(1, "Vitan Cosmin", 1500, "Logistica")
print(employee1)
print(employee1.assign_department("IT"))
print(employee1.employee_details())
print(employee1.calculate_salary(1500, 60))

"""
Clasa MenuItem:
- atribute: id, nume, ingrediente, cantitate, pret, alergeni, categorie
- metode:
    -- print_menu_item - afiseaza detaliile despre preparat
    
Clasa Restaurant:
- atribute: 
    -- nume
    -- menu_items (o lista cu elemente de tip MenuItem)
    -- booked_tables
    
- metode:
    -- add_items_to_menu
    -- delete_item_from_menu
    -- reserve_table
    -- print_menu
    -- print_booked_tables
"""


class MenuItem:

    def __init__(self, id, nume, ingrediente, cantitate, pret, alergeni, categorie):
        self.id = id
        self.nume = nume
        self.ingrediente = ingrediente
        self.cantitate = cantitate
        self.pret = pret
        self.alergeni = alergeni
        self.categorie = categorie

    def print_menu_item(self):
        print(f'ID: {self.id}')
        print(f'Nume: {self.nume}')
        print(f'Ingrediente: {', '.join(self.ingrediente)}')
        print(f'Cantitate kg: {self.cantitate}')
        print(f'Pret: {self.pret}')
        print(f'Alergeni: {', '.join(self.alergeni)}')
        print(f'Categorie: {self.categorie}')


item_1 = MenuItem(1, "Pizza Margherita", ["faina", "sos de rosii", "mozarelle"],
                  1, 24.99, ["gluten", "lactoza"], "Pizza")

item_1.print_menu_item()


class Restaurant:

    def __init__(self, nume):
        self.nume = nume
        self.menu_items = []  # o lista cu elemente de tip MenuItem
        self.booked_tables = set()  # set pentru a urmări mesele rezervate

    def add_items_to_menu(self, menu_item):
        self.menu_items.append(menu_item)  # se adauga noul meniu la lista de meniuri

    def delete_item_from_menu(self, menu_item):
        if menu_item in self.menu_items:
            self.menu_items.remove(menu_item)  # se sterge meniul din lista de meniuri
        else:
            print(f'{menu_item.nume} nu exista in meniu!')

    def reserve_table(self, table_number):
        self.booked_tables.add(table_number)

    def print_menu(self):
        print(f'Meniu pentru restaurantul {self.nume}:')
        for item in self.menu_items:
            item.print_menu_item()

    def print_booked_tables(self):
        print(f'Mesele rezervate la restaurantul {self.nume}: {', '.join(map(str, self.booked_tables))} mese!')


restaurant_1 = Restaurant("Pizza Bella")
restaurant_1.add_items_to_menu(item_1)
restaurant_1.reserve_table(5)
restaurant_1.print_menu()
restaurant_1.print_booked_tables()
"""
3. Clasa BankAccount

- atribute:delete_item_from_menu
    -- account_number
    -- balance
    -- customer_name
    
- metode:
    -- withdraw
    -- deposit
    -- check_balance
"""


class BankAccount:

    def __init__(self, account_number, customer_name):
        self.account_number = account_number
        self.balance = 0
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Depozitat: {amount}. Sold nou: {self.balance}')
        else:
            print("Suma de depozit trebuie sa fie pozitiva!")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Retras: {amount}. Sold nou: {self.balance}')
        else:
            print("Sold insuficient sau suma invalida.")

    def check_balance(self):
        return self.balance


account_1 = BankAccount("123456789", "Gheorghe Vasile")
account_1.deposit(150)
account_1.withdraw(30)
print(f'Sold curent: {account_1.check_balance()}')

"""
4. Implementeaza un decorator care converteste rezultatul returnat de
o functie la int. Daca conversia nu se poate face, trebuie afisat
un mesaj sugestiv ca nu s-a facut conversia (hint: foloseste-te de
try-except in implementarea decoratorului)
"""


# def decorator(func):
#     def wrapper_func(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return int(result)
#         except ZeroDivisionError:
#             print('Nu s-a putut face conversia la int')
#     return wrapper_func()
#
#
# @decorator
# def funct_need_decoration(a, b):
#     return a / b
#
#
# print(funct_need_decoration(0, 5))

"""
5. Implementeaza un decorator ce limiteaza call-ul functiei decorate la 3.
"""




"""
Pentru alte exercitii extra:
- https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/
- https://www.w3resource.com/python-exercises/
- https://www.w3schools.com/python/python_exercises.asp
- https://exercism.org/tracks/python/exercises
"""

# nums = [1, 2, 3]
# print(nums.__iter__())   # <list_iterator object at 0x017AE658>
#
#
# i_nums = iter(nums)
# print(iter(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))


def my_gen():
    n = 1
    print('This is printed first')

    # Generator function contains yield statements
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print('This is printed at last')
    yield n


my_gen()
