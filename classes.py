class Robot_Dog:

    def __init__(self, name, breed): ## __init__ is the equavilent of a constructor
        self.name = name
        self.breed = breed

    def bark(self):
        print('Woof woof!')

class InheritanceTest(Robot_Dog): ## To inherit a class put it in ()

    def bark(self): ## You can override a method by just defining it again
        print('Overridden Woof woof')
    
myDog = Robot_Dog('Diezel', 'Rottweiler')
myDog2 = InheritanceTest('Diezel', 'Rottweiler') ## We inherited the __init__ method so need to write our own one.

print(myDog.breed)
print(myDog.name)
myDog.bark()

print(myDog2.breed)
print(myDog2.name)


myDog2.bark()