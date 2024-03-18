# #Deseneaza un ceas cu broasca testoasa
# import turtle
#
# myScreen=turtle.Screen()
# myScreen.bgcolor('lightblue')
# t=turtle.Turtle()
# t.shape('turtle')
# t.color('blue')
# t.stamp()
#
# for i in range(12):
#     t.penup()
#     t.forward(150)
#     t.stamp()
#     t.backward(150)
#     t.left(30)
    
# players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
#
# #Create 3 lists with 2 players each
# #Use slicing to create a list for Group 1
# g1 = players[0:3]
#
# #Use slicing to create a list for Group 2
# g2 = players[2:4]
#
# #Use slicing to create a list for Group 3
# g3 = players[4:7]
#
# print("Group 1:")
# #display the 1st group
# print(g1)
#
# print("Group 2:")
# #display the 2nd group
# print(g2)
#
# print("Group 3:")
# #display the 3rd group
# print(g3)
#
# weight = int(input())
# def shiping_price(weight):
#     print(weight * 5)
#
# shiping_price(weight)

##################################
def rect(lenght, width):
    area = lenght * width
    perimeter = 2 * lenght + 2 * width
    return area, perimeter

x, y = rect(50, 100)
print(x, y)

print(rect(15, 20))
#######################################
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

a = "Hello, World!"
print(a.replace("l", "J"))
############################  FORMATAREA STRINGURILOR
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
##############################
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
####################################
quantity = 3          #  index 0
itemno = 567          #  index 1
price = 49.95         #  index 2
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#############################
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#############################


class Person:
    def __init__(self, name, age):            # constructorul __init__
        self.name = name
        self.age = age

# p1 = Person("Cosmin", 40)
# print(p1.name)
# print(p1.age)
# p1.name = "Alin"    #am rescris valoarea lui p1
# print(p1.name)

    def __str__(self):
        return f'{self.name}, {self.age}'

    def greet(self):
        print(f'Salut {self.name}, cu varsta {self.age}')


p1 = Person("Raul", 23)
print(p1)
p1.greet()
