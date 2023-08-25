class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def  introduce(self):
        print("Привет меня зовут ", self.name, " мне ", self.age, " лет.")


p1 = Person("Евгений", 21)
p2 = Person("Анатолий", 22)
p3 = Person("Артем", 23)

p1.introduce()
p2.introduce()
p3.introduce()
