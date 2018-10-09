class Square:
    def __init__(self, side):
        self.side = side

    def squareArea(self):
        return self.side ** 2


square1 = Square(10)
print(square1.squareArea())

square_side = int(input("Type square side "))
square2 = Square(square_side)
print(square2.squareArea())



