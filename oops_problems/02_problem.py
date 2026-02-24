# create a class 'pets' from a class 'animal' and further create a class 'dog' from 'pets'. add a method 'bark' to class 'dog'.

class Animal:
    pass

class Pets:
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("bow bow!")


d = Dog()

d.bark()

    