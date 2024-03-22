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
"SMITH", "E7698", 55000, "OPERATIONS".
"""


class Employee:
    # constructor
    def __init__(self, name, id, salary, department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department

    def assign_department(self, new_department):
        self.department = new_department

    def employee_details(self):
        print(f'Ma numesc {self.name}, am id-ul {self.id} '
              f'cu salariul de {self.salary} si lucrez in '
              f'departamentul {self.department}!')

    def calculate_salary(self, hours_worked):
        if hours_worked > 50:
            overtime_pay = (hours_worked - 50) * (self.salary / 50)
            total_salary = overtime_pay + self.salary
        else:
            total_salary = self.salary
        return f'Noul meu salar va fi {total_salary}!'


# Exemple de date pentru angajați
angajat_1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
angajat_2 = Employee("JONES", "E7499", 45000, "RESEARCH")
angajat_3 = Employee("MARTIN", "E7900", 50000, "SALES")
angajat_4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

# Testarea metodelor
angajat_1.assign_department("HR")
angajat_1.employee_details()
print(angajat_1.calculate_salary(60))

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

    #  afiseaza detaliile despre preparat
    def print_menu_item(self):
        print(f"ID: {self.id}")
        print(f"Nume: {self.nume}")
        print(f"Ingrediente: {', '.join(self.ingrediente)}")
        print(f"Cantitate: {self.cantitate}")
        print(f"Pret: ${self.pret}")
        print(f"Alergeni: {', '.join(self.alergeni)}")
        print(f"Categorie: {self.categorie}")
        print()


class Restaurant:
    def __init__(self, nume):
        self.nume = nume
        self.menu_items = []
        self.booked_tables = set()

    def add_items_to_menu(self, menu_item):
        self.menu_items.append(menu_item)

    def delete_item_from_menu(self, item_id):
        self.menu_items = [item for item in self.menu_items if item.item_id != item_id]

    def reserve_table(self, table_number):
        self.booked_tables.add(table_number)

    def print_menu(self):
        print(f'Menu for {self.nume}:')
        for item in self.menu_items:
            item.print_menu_item()

    def print_booked_tables(self):
        print(f'Booked tables for {self.nume}:\n'
              f'{', '.join(map(str, self.booked_tables))}')


# Exemplu de utilizare
menu_item1 = MenuItem(1, "Pizza Margherita", ["dough", "tomato sauce", "mozzarella"],
                      1, 10.99, ["gluten"], "Main Course")
menu_item2 = MenuItem(2, "Tiramisu", ["mascarpone", "ladyfingers", "coffee"],
                      1, 6.99, ["eggs"], "Dessert")

restaurant = Restaurant("La Trattoria")
restaurant.add_items_to_menu(menu_item1)
restaurant.add_items_to_menu(menu_item2)

restaurant.print_menu()
restaurant.reserve_table(5)
restaurant.print_booked_tables()


"""
3. Clasa BankAccount

- atribute:
    -- account_number
    -- balance
    -- customer_name
    
- metode:
    -- withdraw
    -- deposit
    -- check_balance
"""

"""
4. Implementeaza un decorator care converteste rezultatul returnat de
o functie la int. Daca conversia nu se poate face, trebuie afisat
un mesaj sugestiv ca nu s-a facut conversia (hint: foloseste-te de
try-except in implementarea decoratorului)
"""

"""
5. Implementeaza un decorator ce limiteaza call-ul functiei decorate la 3.
"""


class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name

    def withdraw(self, valoarea_retrasa):
        if self.balance >= valoarea_retrasa:
            print(f'Retragerea sumei de {valoarea_retrasa} încheiata cu succes!')
            print(f'Suma rămasa in cont este: {self.balance} Ron')
        else:
            print('')

    def deposit(self):
        pass

    def check_balance(self):
        pass


"""
Pentru alte exercitii extra:
- https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/
- https://www.w3resource.com/python-exercises/
- https://www.w3schools.com/python/python_exercises.asp
- https://exercism.org/tracks/python/exercises
"""