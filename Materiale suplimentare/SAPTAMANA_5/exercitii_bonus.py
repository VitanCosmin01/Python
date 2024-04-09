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


class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name

    def __str__(self):
        return f'{self.account_number}, {self.balance}, {self.customer_name}'

    def withdraw(self, valoarea_retrasa):
        if self.balance >= valoarea_retrasa:
            print(f'Retragerea sumei de {valoarea_retrasa} RON încheiata cu succes!')
            self.balance = self.balance - valoarea_retrasa
            print(f'Suma rămasa in cont este: {self.balance} Ron')
        else:
            print('Valoarea este mai mare decat balanta! Incercati o valoare mai mica!')

    def deposit(self, valoarea_depusa):
        self.balance = self.balance + valoarea_depusa
        print(f'Valoarea depusa este {valoarea_depusa} RON!')
        print(f'Valoarea totala a contului este {self.balance} RON!')

    def check_balance(self):
        print(f'Balanta actuala este {self.balance} RON !')


count1 = BankAccount(112233, 5000, "Vitan Cosmin")
print(count1)
count1.withdraw(500)
count1.deposit(1500)
count1.check_balance()
# Example usage
if __name__ == "__main__":
    account = BankAccount(112233, 6000, "Vitan Cosmin")
    account.deposit(1000)
    account.withdraw(200)
    account.check_balance()
"""
4. Implementeaza un decorator care converteste rezultatul returnat de
o functie la int. Daca conversia nu se poate face, trebuie afisat
un mesaj sugestiv ca nu s-a facut conversia (hint: foloseste-te de
try-except in implementarea decoratorului)
"""


def int_converter(func):
    """
    Decorator care convertește rezultatul unei funcții la un număr întreg.
    Dacă conversia eșuează, se afișează un mesaj.
    """

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            int_result = int(result)
            return int_result
        except ValueError:
            print(f"Conversia la întreg a eșuat pentru rezultatul: {result}")
            return None

    return wrapper


# Exemplu de utilizare a decoratorului
@int_converter
def divide(a, b):
    return a / b


# Testează funcția decorată
result = divide(10, 3)
print(f"Rezultat după conversie: {result}")

"""
5. Implementeaza un decorator ce limiteaza call-ul functiei decorate la 3.
"""


def limit_calls(max_calls):
    """
    Decorator care limitează numărul de apeluri la funcția decorată.
    :param max_calls: Numărul maxim de apeluri permise.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.call_count < max_calls:
                wrapper.call_count += 1
                return func(*args, **kwargs)
            else:
                raise ValueError(f"Funcția {func.__name__} a atins numărul maxim de apeluri permise.")

        wrapper.call_count = 0
        return wrapper

    return decorator


# Exemplu de utilizare
@limit_calls(max_calls=5)
def salut(nume):
    print(f"Salut, {nume}!")


salut("Alice")  # Apel 1
salut("Bob")  # Apel 2
salut("Charlie")  # Apel 3
salut("David")  # Ridică o excepție ValueError
"""
Pentru alte exercitii extra:
- https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/
- https://www.w3resource.com/python-exercises/
- https://www.w3schools.com/python/python_exercises.asp
- https://exercism.org/tracks/python/exercises
"""


def my_first_decorator(function_as_parameter):
    def wrapper_func(*args, **kwargs):
        print(f'Am intrat in functia {function_as_parameter.__name__}!!!')
        function_as_parameter(*args, **kwargs)
        print(f'Am iesit din functia {function_as_parameter.__name__}!!!')

    return wrapper_func


@my_first_decorator
def need_decorator(nume="Cosmin"):
    print(f'Hello my brother {nume} !')


need_decorator()



