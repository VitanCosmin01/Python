# base class / parent class
class Chef:  # clasa parinte

    def __init__(self, experience):
        self.experience = experience

    def make_salad(self):
        print("salad")

    def make_fries(self):
        print("fries")


# child class - mosteneste din clasa Chef
# se trece intre paranteze numele clasei parinte
class JapaneseChef(Chef):  # clasa copil

    def make_sushi(self):
        print("sushi")


# child class - mosteneste din clasa Chef
# se trece intre paranteze numele clasei parinte
class ItalianChef(Chef):

    def make_pizza(self):
        print("pizza")


# chef1 = Chef(2)
# # chef1.make_sushi()
# chef1.make_salad()
# chef1.make_fries()
# print(chef1.experience)
#
# chef2 = JapaneseChef(15)
# chef2.make_sushi()
#
# chef2.make_salad()
# chef2.make_fries()
# print(chef2.experience)
#
# chef3 = ItalianChef(23)
# chef3.make_pizza()
# #
# chef3.make_salad()
# chef3.make_fries()
# print(chef3.experience)

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Animal {self.name} has {self.age} years old.")


class Dog(Animal):

    # Pentru a adauga proprietati noi:
    # 1. Extindem lista de parametrii pe care
    # metoda __init__ ii poate lua.
    # 2. Apelam __init__-ul din clasa parinte, folosindu-ne de
    # super(), cu parametrii pentrunecesari pentru clasa parinte.
    def __init__(self, name, age, sound, color):
        super().__init__(name, age)
        self.sound = sound
        self.color = color

    # Pentru a extinde metode din clasa parinte:
    # Facem apel la metoda din clasa parinte folosind super()
    def describe(self):
        super().describe()
        print(f"Animal's color is {self.color}.")
        print(f"He says: {self.sound}.")


animal = Animal(name="John", age=5)
# print(animal.age)
# print(animal.name)
# animal.describe()

dog1 = Dog(
    name="Max",
    age="12",
    sound="ham ham",
    color="black"
)

# print(dog1.name)
# print(dog1.age)
# print(dog1.sound)
# print(dog1.color)
#
# dog1.describe()

"""
EX1: MOSTENIRE
a. Defineste o clasa numita Persoana.
Aceasta clasa va avea urmatoarele atribute (in constructor):
- nume
- varsta

Implementeaza metoda descrie(), care va afisa mesajul:
'Persoana {nume} are {varsta} ani.'

b. Defineste clasa Angajat, care mosteneste din clasa Persoana.
Aceasta clasa va lua in constructor inca doi parametri,
salariu si post.
Defineste metoda afiseaza_salariu, care returneaza
atributul salariu.

c. Creeaza un obiect de tip clasa Persoana.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metoda descrie.

d. Creeaza un obiect de tip Angajat.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metodele disponibile pe aceasta.

e. Extinde metoda descrie din clasa Angajat,
astfel incat sa se afiseze
si o propozitie care contine atributele salariu si post.
"""


class Persoana:

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def descrie(self):
        print(f"Persoana {self.nume} are {self.varsta} ani.")


class Angajat(Persoana):

    def __init__(self, nume, varsta, salariu, post):
        super().__init__(nume, varsta)
        self.salariu = salariu
        self.post = post

    def afiseaza_salariu(self):
        return self.salariu

    def descrie(self):
        super().descrie()
        print(f"Angajatul are salariul de {self.salariu} pentru postul de {self.post}!")


pers1 = Persoana("Comy", 40)
print(pers1.varsta)
print(pers1.nume)
pers1.descrie()

print("Punctul d: ________________")

angajat1 = Angajat("Ion", 19, 2100, "mecanic")
print(angajat1.varsta)
print(angajat1.nume)
print(angajat1.post)
print(angajat1.salariu)
angajat1.afiseaza_salariu()
angajat1.descrie()
print(
    f"{angajat1.nume} are salariul de {angajat1.salariu} si are "
    f"salariul de {angajat1.salariu} si meseria de {angajat1.post}.")
print("_________________________")


# POLIMORFISM

# Exemplu de class methods polimorfice
class Romania:
    def language(self):
        print("Romanian")

class USA:
    def language(self):
        print("English")

obj_ro = Romania()
obj_usa = USA()

obj_ro.language()     # => Romanian
obj_usa.language()    # => English

def get_country_language(country_obj):
    country_obj.language()

get_country_language(obj_ro)   # => Romanian
get_country_language(obj_usa)  # => English

print("____________________________________")

# ABSTRACTIZAREA
# Se importa:
from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def describe(self):
        print("This animal is my favourite!")


class Dog(Animal):

    def sound(self):
        print("Ham ham")

    def sleep(self):
        print('ZZZZ')
class Cat(Animal):

    def sound(self):
        print("Miau miau")

    def sleep(self):
        print("Prrrr")


cat = Cat()
cat.sound()    # => Miau miau
cat.sleep()     # => Prrr
cat.describe()  # => This animal is my favourite!

dog = Dog()
dog.sound()   # =>Ham ham
dog.sleep()   # =>ZZZZ
dog.describe()  # =>This animal is my favourite!
print("_____________________Ex:_3______________")
#from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def car_model(self):
        pass


class Tesla(Car):
    def __init__(self, model):
        self.model = model

    def car_model(self):
        print(f"This is an electric car {self.model}")


class Bmw(Car):
    def __init__(self, model):
        self.model = model

    def car_model(self):
        print(f"Stupid car {self.model}")


bmw = Bmw("E46")
bmw.car_model()

tesla = Tesla("S3")
tesla.car_model()

print("_____________________________________")
# Incapsulare


class Car:

    def __init__(self, brand, price):
        self.__brand = brand  # atribut privat
        self._price = price  # atribut protected

    def run(self):
        print(f"Please run {self.__brand}")


car = Car("Dacia", 5000)

# print(car.__brand) # -> eroare
print(car._price)
car.run()
###############################################


class Car:
    __color = 'grey'

    def get_color(self):  # folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoarea_dorita):  # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita


##################################################
class User:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def get_password(self):
        return "*" * len(self.__password)

    def set_password(self, new_password):
        # Criterii de setare parola
        # - are cel putin o litera mare
        # - are cel putin un numar
        # - are minim 10 caractere
        if len(new_password) < 10:
            print("Parola noua trebuie sa aiba 10 caractere!")
            return
        for caracter in new_password:
            # if caracter == caracter.upper():
            #     break

            if caracter.isupper():
                break
        # for index in range(0, len(new_password)):
        #     if new_password[index] == new_password[index].upper():
        #         break
        self.__password = new_password


# my_str = "abc"
# my_str.isupper()

user1 = User("cosminabacter", "cosmina@gmail.com", "123")
print(user1.email)
print(user1.username)
# print(user1.__password)
print(user1.get_password())

user1.set_password("cosmina")
print(user1.get_password())

print("_________________EX_4_______________________")

# se importa:
# from abc import ABC, abstractmetod

"""
EX4: ENCAPSULARE
a. Defineste o clasa Produs.
Aceasta va avea in constructor urmatoarele atribute:
- nume
- pret
- discount - atribut privat

b. Defineste proprietatea discount:
- getter
- setter -> inainte de a seta o valoare pentru discount,
asigura-te ca acesta e cuprins intre 0-100.
- deleter
"""


class Produs:
    def __init__(self, nume, pret, discount):
        self.nume = nume
        self.pret = pret
        self.__discount = discount

    def get_discount(self):
        return self.__discount

    def set_discount(self, new_discount):
        if 0 < new_discount <= 100:
            return new_discount
        else:
            print(f"Valoarea {self.__discount} este mai mare decat 100")
        self.__discount = new_discount

    def del_discount(self):
        print("Discount deleted")
        self.__discount = None


prod1 = Produs("masa", 200, 101)  # am creat un obiect
print(prod1.nume)                                   # am acccesat atributele pe obiect
print(prod1.pret)                                   # am acccesat atributele pe obiect
# print(prod1.get_discount())

Produs.set_discount(prod1,120)
print(prod1.get_discount())

Produs.del_discount(prod1)
print(prod1.get_discount())

####################################

print("Try/Except exemple")

numar = int(input("Introdu un numar: "))
rezultat = 0
try:
    rezultat = 10 / numar
except ZeroDivisionError:
    print("Nu se poate face impartirea la 0.")
else:
    # se intra in blocul else doar daca nu s-a aruncat o exceptie
    print()
finally:
    # OPTIONAL: indiferent daca se arunca exceptie sau nu,
    # acest bloc este executat.
    print("finally se executa mereu")
print(rezultat)
#####################################################


# from abc(AbstractBaseClass Library) import ABC(este o clasa), abstractmethod(este o functie)

class CarABC(ABC):

    @abstractmethod
    def describe(self):
        pass

    def accelerate(self):
        return 50
