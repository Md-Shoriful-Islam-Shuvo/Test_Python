import math

# Create the Shape parent class
class Shape:
    def __init__(self, color):
        self.color = color
    def area(self):
        return 0
    def describe(self):
        print(f"This is a {self.color} shape.")
    def shape_type(self):
        print("This is a shape class")

# Create the Circle child class
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def describe(self):
        #super().describe()
        print(f"This is a {self.color} circle with radius {self.radius}.")

# Create the Square child class
class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    def describe(self):
        #super().describe()
        print(f"This is a {self.color} square with side length {self.side_length}.")

#example usage
circle = Circle("red", 5)
square = Square("blue", 4)
shape = Shape("green")
print(f"Circle area: {circle.area():.02f}")
print(f"Square area: {square.area()}")
print(f"Shape area: {shape.area()}")
circle.describe()
square.describe()   
shape.describe()

class t(Circle):
    pass


t1 = t("green", 2)
t1.describe()
t1.shape_type