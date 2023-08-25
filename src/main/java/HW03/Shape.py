class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Рисование круга")


class Rectangle(Shape):
    def draw(self):
        print("Рисование прямоугольника")


class Triangle(Shape):
    def draw(self):
        print("Рисование треугольника")


class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "круг":
            return Circle()
        elif shape_type == "прямоугольник":
            return Rectangle()
        elif shape_type == "треугольник":
            return Triangle()
        else:
            raise ValueError("Нет такой фигуры")



shape_factory = ShapeFactory()
circle = shape_factory.create_shape("круг")
rectangle = shape_factory.create_shape("прямоугольник")
triangle = shape_factory.create_shape("треугольник")

circle.draw()
rectangle.draw()
triangle.draw()