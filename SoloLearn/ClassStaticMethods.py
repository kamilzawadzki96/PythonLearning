class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    @classmethod
    def new_square(cls, side_length):
        calculated = cls(side_length, side_length)
        return calculated

square = Rectangle.new_square(10)
print(square.area())