class Animal:
    def __init__(self, name):
        self.name = name

    def drink(self):
        print(f"{self.name} is drinking.")

    def eat(self):
        print(f"{self.name} is eating.")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping.")

animal = Animal("Jimmy")

frog = Frog("Hoppy")

print(animal.name)
animal.drink()
animal.eat()

print(frog.name)
frog.drink()
frog.eat()
frog.jump()




