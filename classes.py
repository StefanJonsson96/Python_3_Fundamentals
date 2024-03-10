class Robot_Dog:

    def __init__(self, name, breed): ## __init__ is the equavilent of a constructor
        self.name = name
        self.breed = breed

    def bark(self):
        print('Woof woof!')

myDog = Robot_Dog('Diezel', 'Rottweiler')

print(myDog.breed)
print(myDog.name)

myDog.bark()