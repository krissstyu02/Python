#ЛР 13.1-13.3
# #13.1 Создайте класс Cat. Определите атрибуты name (имя), color
# (цвет) и weight (вес). Добавьте метод под названием meow («мяуканье»).
# Создайте объект класса Сat, установите атрибуты, вызовите метод meow.

class Cat():
    name="" # имя кота
    color=""
    weight=0 # вес
# Первым аргументом любого метода всегда является self, т.е. сам объект
    def meow(self): # функция внутри класса называется методом
       print(self.name, "Сказал мяу")

myCat = Cat()
myCat.name = "Барсик"
myCat.weight = 5
myCat.color = "Серый в полоску"
myCat.meow()

# 13.2#Напишите код, описывающий класс Animal:
# • добавьте атрибут имени животного;
# • добавьте метод eat(), выводящий «Намнём»;
# • добавьте методы getName() и setName();
# • добавьте метод makeNoise(), выводящий «Имя животного говорит
# Гррр»;
# • добавьте конструктор классу Animal, выводящий «Родилось животное
# имя животного».
# Основная программа:
# • создайте животное, в момент создания определите его имя;
# • узнайте имя животного через вызов метода getName();
# • измените имя животного через вызов метода setName();
# • вызовите eat() и makeNoise() для животного.

class Animal():
    name=""
    def __init__ (self, newName):
        self.name = newName
        print("Родилось животное",self.name)
    def eat(self):
       print("Давайте Намнем!")
# Можем в любой момент вызвать метод и изменить имя собаки
    def setName(self, newName):
        self.name = newName
# Можем в любой момент вызвать метод и узнать имя собаки
    def getName (self):
        return self.name # возвращаем текущее имя объекта
    def makeNoise(self): # функция внутри класса называется методом
        print(self.name, "говорит Грр")

# Создаем собаку с начальным именем:
myAnimal = Animal ("Обезьяна")
print (myAnimal.getName())
# Установим новое имя собаки:
myAnimal.setName("Кот")
myAnimal.eat()
myAnimal.makeNoise()

# #13.3 Задание 3 Создайте класс StringVar для работы со строковым типом
# данных, содержащий методы set() и get(). Метод set() служит для изменения
# содержимого строки, get() – для получения содержимого строки. Создайте
# объект типа StringVar и протестируйте его методы.
class StringVar():
    text = ""

    def __init__(self, newText):
        self.text = newText

    def set(self, newText):
        self.text = newText

    def get(self):
        return self.text

myString = StringVar("Моего кота зовут Барсик")
print(myString.get())
print("Это неправда!")
myString.set(input("Его зовут Барс!\n"))
print(myString.get())



