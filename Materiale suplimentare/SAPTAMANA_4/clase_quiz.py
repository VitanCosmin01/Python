
# 1: Cum se verifică tipul obiectului clasei?


class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


class Bus:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


a3 = Car("Q3", "Audi")
v9 = Bus("V9400", "Volvo")

print(type(a3))    # class <'__main__.car'>
print(type(v9))    # class <'__main__.bus'>


# 2: Cum să verificăm dacă un obiect este instanța clasei?

class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


class Bus:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


a3 = Car("Q3", "Audi")
v9 = Bus("V9400", "Volvo")

print(isinstance(a3, Car))    # True
print(isinstance(v9, Car))    # False


#  3: Definiți un atribut comun de clasă pentru toate clasele.


class Car:
    brand = "Audi"

    def __init__(self, name, engine):
        self.name = name
        self.engine = engine


q5 = Car("Q5", "Petrol")
d6 = Car("D6", "Diesel")

print(q5.brand)    # Audi
print(q5.name)     # Q5

print(d6.brand)    # Audi
print(d6.engine)   # Diesel
