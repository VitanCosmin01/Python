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
5. Implementeaza un decorator ca limiteaza call-ul functiei decorate la 3.
"""

"""
Pentru alte exercitii extra:
- https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/
- https://www.w3resource.com/python-exercises/
- https://www.w3schools.com/python/python_exercises.asp
- https://exercism.org/tracks/python/exercises
"""