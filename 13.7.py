# #Основная программа. Код, создающий кота, двух собак и
# одно простое животное. Дайте имя каждому животному (через вызов методов).
# Код, вызывающий eat() и makeNoise() для каждого животного.

class Animal():
    name = ""
    def __init__(self,newName):
        self.name = newName
    def setName(self, newName):
        self.name = newName
    def getName(self):
        print(self.name)


class Dog(Animal):
    def makeNoise(self):
        print(self.name, " говорит Гав")
    def eat(self):
        print(self.name, "грызет кость")

class Cat(Animal):

    def makeNoise(self):
        print(self.name, " говорит мяу")
    def eat(self):
        print(self.name, " скушал ящерицу")

class Kapibara(Animal):
    def makeNoise(self):
        print(self.name, "рычит ррр")
    def eat(self):
        print(self.name, " вкусно покушала")

MyCat = Cat("Барсик")
MyCat.setName("Барс")
MyCat.getName()
MyCat.eat()
MyCat.makeNoise()

Dog1 = Dog("Бублик")
Dog1.getName()
Dog1.eat()
Dog1.makeNoise()

Dog2 = Dog("Тигр")
Dog2.getName()
Dog2.eat()
Dog2.makeNoise()

Kapibarka = Kapibara("Зоя")
Kapibarka.getName()
Kapibarka.eat()
Kapibarka.makeNoise()

