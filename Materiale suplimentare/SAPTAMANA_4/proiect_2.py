"""
TodoList
    Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol

     Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizează_task(nume) - se va sterge din dict
afișează_todo_list() - doar cheile

Ramane ca TEMA (nu modificati fisierul acesta, faceti unul la voi in folder):
afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
    Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
    Dacă acesta răspunde nu - la revedere
    Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
"""


class TodoList:
    def init(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

task = TodoList()
task.adauga_task('curatenie', 'la ora 10')
print(task.todo)
task.adauga_task('cumparaturi', 'la salar')
print(task.todo)
###########################
class TodoList:
    def init(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        if nume in self.todo:
            del self.todo[nume]
        else:
            print("nu a sters")

    def afiseaza_todo_list(self):
        for asd in self.todo.keys():
            print(asd)

    # def afiseaza_todo_list(self):
    #     print(list(self.todo.keys()))

task = TodoList()
task.adauga_task("curatenie", "la ora 10")
print(task.todo)
task.adauga_task("cumparaturi", "la salar")
print(task.todo)
task.finalizeaza_task("curatenie")
print(task.todo)
task.finalizeaza_task("bani")
print(task.todo)
task.adauga_task("sedinta", "strada_primaverii")
task.adauga_task("zii de nastere", "la_george")
task.afiseaza_todo_list()
