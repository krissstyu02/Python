# #13.4 Задание 4 Создайте класс точка Point, позволяющий работать с
# координатами ( , ). Добавьте необходимые методы класса.

class Point():
    pos_x = 0
    pos_y = 0

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def show_pos(self):
        print("Координаты точки:(", self.pos_x, ",", self.pos_y,")")

    def del_pos(self):  # обнулить точку
        self.pos_x = 0
        self.pos_y = 0

    def setPosX(self, x):  # изменить x отдельно
        self.pos_x = x

    def setPosY(self, y):  # изменить y отдельно
        self.pos_y = y

    def setPoint(self, x, y):  # задать точку целиком
        self.pos_x = x
        self.pos_y = y


newPoint = Point(1, 4)
newPoint.show_pos()
newPoint.del_pos()
newPoint.show_pos()
newPoint.setPosX(10)
newPoint.show_pos()
newPoint.setPosY(10)
newPoint.show_pos()
newPoint.setPoint(1000, 1000)
newPoint.show_pos()

# #13.5 Пусть Animal будет родительским для класса Cat. Метод
# makeNoise() класса Cat выводит «Имя животного говорит Мяу». Конструктор
# класса Cat выводит «Родился кот», а также вызывает родительский
# конструктор.

class Animal():
    def __init__(self):
        print("Родилось животное")


class Cat(Animal):
    name = ""

    def __init__(self, newName = ""):
        self.name = newName
        print("Родился кот", self.name)
        Animal.__init__(self)

    def makeNoise(self):
        print(self.name, " говорит Мяу")


newCat = Cat()
Барс = Cat("Барс")
Барс.makeNoise()

# #13.6 Пусть Animal будет родительским для класса Dog. Метод
# makeNoise() для Dog выводит «Имя животного говорит Гав». Конструктор Dog
# выводит «Родилась собака», а также вызывает родительский конструктор.
class Dog(Animal):
    name = ""

    def __init__(self, newName = ""):
        self.name = newName
        print("Родилась собака", self.name)
        Animal.__init__(self)

    def makeNoise2(self):
        print(self.name, " говорит Гав")


newDog = Dog()
Бублик = Dog("Бублик")
Бублик.makeNoise2()

