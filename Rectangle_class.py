class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


square_side = int(input("Type square side "))
square2 = Square(square_side)
print(square2.area())

rectangle_side_a = int(input("Type rectangle side a "))
rectangle_side_b = int(input("Type rectangle side b "))
rectangle = Rectangle(rectangle_side_a, rectangle_side_b)
print(rectangle.area())