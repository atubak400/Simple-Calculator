""""INHERITANCE Part 1"""
print("INHERITANCE PART 1")
print("")

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print(f"I don't know what to say")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

    def play(self):
        print("I love football")

class Mouse(Pet):
    pass

bingo = Dog("Bingo", 4)
bingo.show()
bingo.speak()
bingo.play()

Mouse = Pet("Mouse", 12)
Mouse.speak()

Bear = Pet("Bear", 21)
Bear.speak()
#Bear.play()   #Error: Parent doesnt inherit from child




print("")
print("")
""""INHERITANCE Part 2"""
print("INHERITANCE PART 2")
print("")

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I am {self.color}")

    def speak(self):
        print(f"I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self, amount):
        print("Meow", self.name, "meow", amount*4)   # name is coming from parent class and amount is an object arguement



Lina = Cat("Lina", 7, "yellow")
Lina.show()
Lina.speak(20)