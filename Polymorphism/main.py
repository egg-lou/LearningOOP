class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def make_animal_speak(animal):
    return animal.speak()


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    
    animals = [dog, cat]
    
    for animal in animals:
        print(make_animal_speak(animal))
