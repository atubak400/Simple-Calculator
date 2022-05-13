print("Example 1")
print("The concept of OOP, Class and Methods")
print("")
class Warriors:

    def distance_shootung(self):
        print("Has the ability to shoot full court")
        print("Has the ability to shoot half court")
        print("Has the ability to shoot 3pts")

    def runner(self):
        print("Has the ability to keep running and not get tired")
        print("Has the ability to chase down opponents for the entirety of the game")

    def clutch(self, x):
        print(f"{x} is calm under immense pressure")
        print(f"{x} shoots very accurately at the late stages of the game")
        print(f"{x} is less recklesswith the ball than most other players")


Curry = Warriors()
Curry.distance_shootung()
Klay = Warriors()
Klay.clutch("Klay")


print("")
print("")
print("Example 2")
print("Defining/Initializing your class")
print("")
class Warriors:

    def __init__ (self, name, age):
        self.name = name
        self.age = age
        print(name)


Curry = Warriors("Curry", 32)


print("")
print("")
print("Example 3")
print("Passing down variables fromyour class to your methods")
print("")
class Warriors:

    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.isLightSkin = True  #note isLightSkin is not an __init__ parameter. It's allowed.

    def get_name(self):
        print(f"They call him {self.name}")
     

    def get_age(self):
        print(f"He is {self.age} years old")
        
    def set_age(self, age):
        self.age = age
        print(f"Age has been changed to {self.age} successfully")
        
    def get_introduction(self):
        print(f"{self.name} is {self.age} years old")
        print(f"{self.isLightSkin} {self.name} is a light skin dude")


Curry = Warriors("Steph Curry", 32)
Curry.get_name()
Curry.get_age()
Curry.get_introduction()

print("")
Klay = Warriors("Klay Thompson", 32)
Klay.get_name()
Klay.get_age()
Klay.get_introduction()
Klay.set_age(31)
Klay.get_introduction()




