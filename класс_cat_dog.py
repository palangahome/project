class Animal:
    def make_a_sound(self):
        print("Издаёт животный звук")
        
class Cat(Animal):
    def drop_everything(self):
        print('Вставай скорее, я всё уронил!')


class Dog(Animal):
    def dig_the_ground(self):
        print('Однажды я докопаюсь до ядра планеты!')
    def make_a_sound(self):
        print('Гав-гав!')
        
Tom=Dog()
Tom.make_a_sound()