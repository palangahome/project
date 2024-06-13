'''
Обратите внимание на метод __init__ класса GreetingMix. В нём вместо вызова метода базового класса через функцию super() используется непосредственный вызов из базовых классов с указанием имён этих классов. Такой вызов необходим из-за того, что метод __init__ присутствует в обоих базовых классах и происходит конфликт. Интерпретатор при использовании функции super() в нашем примере использовал бы метод того класса, который стоит левее при перечислении в объявлении производного класса. В нашем примере это привело бы к тому, что __init__ из класса GreetingInformal не был бы вызван и в производном классе не произошла бы инициализация атрибута informal_greeting. Тогда при вызове метода greet_informal было бы вызвано исключение AttributeError.
'''

class GreetingFormal:

    def __init__(self):
        self.formal_greeting = "Добрый день,"

    def greet_formal(self, name):
        return f"{self.formal_greeting} {name}!"


class GreetingInformal:

    def __init__(self):
        self.informal_greeting = "Привет,"

    def greet_informal(self, name):
        return f"{self.informal_greeting} {name}!"


class GreetingMix(GreetingFormal, GreetingInformal):

    def __init__(self):
        GreetingFormal.__init__(self)
        GreetingInformal.__init__(self)


mixed_greeting = GreetingMix()
print(mixed_greeting.greet_formal("Пользователь"))
print(mixed_greeting.greet_informal("Пользователь"))