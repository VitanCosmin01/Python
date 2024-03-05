# class Car:
#
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         print("Getter")
#         if self.__color is not None:
#             return self.__color.upper()
#         return "nu avem culoare"
#
#     # @color.getter
#     # def color(self):
#     #     print("Getter")
#     #     if self.__color is not None:
#     #         return self.__color.upper()
#     #     return "nu avem culoare"
#
#     @color.setter
#     def color(self, culoare_noua):
#         print("Setter")
#         self.__color = culoare_noua
#
#     @color.deleter
#     def color(self):
#         print("Deleter")
#         self.__color = None
#
#
#
# car1 = Car("rosu")
# print(car1.color)
#
# car1.color = "verde"
# print(car1.color)
#
# del car1.color
# print(car1.color)

# class Person:
# 
#     def __init__(self, name, cnp, age, height):
#         self.name = name
#         self.__cnp = cnp # atribut privat
#         self.age = age
#         self.height = height
# 
#     @property
#     def cnp(self):
#         print("Getter cnp")
#         return self.__cnp
# 
#     @cnp.setter
#     def cnp(self, new_cnp):
#         print("Setter cnp")
#         if len(new_cnp) == 13:
#             self.__cnp = new_cnp
#         else:
#             print("Invalid CNP value")
# 
# 
# person1 = Person("George", "1970629204466", 26, 170)
# print(person1.cnp)
# person1.cnp = "1970629"
# print(person1.cnp)
# person1.cnp = "1970629204467"
# print(person1.cnp)
# # print(person1.__cnp)

"""
EX5: Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""
from abc import ABC, abstractmethod


class AbstractVideo:
    def __init__(self) -> object:
        pass

    @abstractmethod
    def show_details(self):
        pass

    def play(self):
        print("Video is playing.")


"""
EX6: Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""


class Videoclip(AbstractVideo):

    def __init__(self, title, duration):
        super().__init__()
        self.title = title
        self.duration = duration

    def show_details(self):
        print(f'{self.title} has a duration of {self.duration} minutes.')


movie_1 = Videoclip("Avatar", 180)
print(movie_1.title)
print(movie_1.duration)
Videoclip.show_details(movie_1)
Videoclip.play(movie_1)
"""
EX7:
a. Defineste o clasa numita Movie care va mosteni clasa Videoclip.
Extinde constructorul/metoda de initializare a clasei Movie,
astfel incat sa aiba ca atribute si :
- genre (str)
- director (str) -> ATRIBUT PRIVAT!
- actors (list)

b. Extinde metoda show details, astfel incat sa se afiseze si
mesajul: 
'Is directed by {director} and the actors are {actors}.'

c. Defineste o proprietate director, cu getter, setter si deleter,
care incapsuleaza atributul privat __director.
"""


class Movie(Videoclip):

    def __init__(self, genre, director, actors, title, duration):
        super().__init__(title, duration)
        self.genre = genre
        self.__director = director
        self.actors = actors

    # _____B_______
    def show_details(self):
        super().show_details()
        print(f"Is directed by {self.__director} and the actors are {self.actors}.")


movie_2 = AbstractVideo()
print(movie_2.play())