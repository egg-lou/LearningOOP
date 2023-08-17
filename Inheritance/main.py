# Define a base class called "Animal"
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # This method will be overridden in subclasses


# Define a subclass "Dog" that inherits from "Animal"
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# Define a subclass "Cat" that inherits from "Animal"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


if __name__ == "__main__":
    # Create an instance of "Dog" class
    dog = Dog("Buddy")
    # Create an instance of "Cat" class
    cat = Cat("Whiskers")
    
    # Call the "speak" method of "Dog" class
    print(dog.speak())  # Output: Buddy says Woof!
    # Call the "speak" method of "Cat" class
    print(cat.speak())  # Output: Whiskers says Meow!
