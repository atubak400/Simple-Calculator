""""CLASS ATTRIBUTES"""
print("CLASS ATTRIBUTES")
print("")

class Person:
    number_of_people = 0

    def __init__(self, fullname):
        self.fullname = fullname
        Person.number_of_people += 1

Curry = Person("Steph Curry") #this initialization increases number of people by 1
print(Curry.fullname)
print(Curry.number_of_people)
Klay = Person("Klay Thompson") #this also increases it by 1, making it two people now
print(Klay.fullname)
print(Klay.number_of_people)




print("")
print("")
""""CLASS METHODS"""
print("CLASS METHODS")
print("")

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people



Curry = Person("Steph Curry") #this initialization increases number of people by 1
Klay = Person("Klay Thompson") #this also increases it by 1, making it 2 people now
print(f"Numbe of people = {Person.number_of_people_()}")




print("")
print("")
""""STATIC METHODS"""
print("STATIC METHODS")
print("")

class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")



print(Math.add5(20))
print(Math.add10(30))
Math.pr()