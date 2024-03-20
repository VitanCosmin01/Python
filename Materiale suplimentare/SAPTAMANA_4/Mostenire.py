#  clasa parinte
class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print("Hi " + self.fname + "!")


#  clasa copil
class Student(Person):

    def __init__(self, fname, lname, age, school):
        #  call super() funtion
        super().__init__(fname, lname)
        self.age = age
        self.school = school

    def greet(self):
        print("Good morning!")
        print(f'I am student {self.fname} {self.lname} having the age {self.age}!')
        print(f'I am learning at school {self.school}!')


p = Person("Cosmin", "Vitan")
p.display()
s = Student("Raul", "Vitan", 21, "It Factory")
s.greet()
s.display()

