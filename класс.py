class Human:
    def __init__(self, name, age, iq):
        self.name = name
        self.age = age
        self.iq = iq
    def showInfo(self):
        print(self.name,self.age,self.iq)

class Worker(Human):
    def __init__(self,name, age, iq, salary, dolzhnost, stazh):
        super().__init__(name, age, iq)
        self.salary = salary
        self.dolzhnost = dolzhnost
        self.stazh = stazh

petia = Human('Петя', 20, 100)
vasia = Human('Вася', 30, 77)

kolya= Worker(name='Коля',age=31,iq=78,dolzhnost='Программист',salary=100000, stazh=0.5)
kolya.showInfo()



petia.showInfo()
vasia.showInfo()