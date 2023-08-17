from abc import ABC, abstractmethod

# Define an abstract base class "Shape"
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Define a concrete subclass "Circle" that inherits from "Shape"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2


# Define a concrete subclass "Rectangle" that inherits from "Shape"
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    print("Circle Area:", circle.area())  # Output: Circle Area: 78.53975
    print("Rectangle Area:", rectangle.area())  # Output: Rectangle Area: 24
