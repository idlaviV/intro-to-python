## Functions 2
# lambda, filter & map

# Pyhton supports lambda functions - which in python are just functions which
# do not need a descriptor (name)
# this is a valid lambda function
lambda x: print(x)

# we can assign this function to a variable and use it
p = lambda x: print(x)
p("hello")


# lambda function are realy usefull for the filter and map functions:
# map: apply a function to every element in a list:
meassures = [1, 41, 1212.133, 14.654]
# syntax: map(function, list)
result = map(int, meassures)
print(result)

# the map call returns a map object and has to be converted to a list again
# like this:
meassures = list(map(int, meassures))
print(meassures)

# or this:
meassures = [1, 41, 1212.133, 14.654]
meassures = [*map(int, meassures)]
print(meassures)

# if we want to use our own function, we can simply use lambda functions:
meassures = [*map(lambda x: x + 1, meassures)]
print(meassures)


# using the same syntax we can filter:
meassures = [*map(lambda x: x > 3, meassures)]
print(meassures)

## Classes
# Almost everything in Python is an object, with its properties and methods.
# A class is the blueprint for an object - an object is an instance of a class
# (isinstance function).
# A class has properties and methods (functions belonging to a class).

class Human:
    """
    docstring for Human.
    Her we can describe what the class is about.
    """

    # this is the constructor - which gets executed when we initialize 
    # a new object with all the arguments we pass
    def __init__(self, name, birth_date):
        # The self parameter is a reference to the current instance of the class
        # and is used to access variables/properties & methods 
        # that belongs to the class.
        self.name = name
        self.birth_date = birth_date
        self.age = 0
        self.dead = False
    
    # class methods always need the self parameter as the first parameter
    def birthday(self):
        if not self.is_dead():
            self.age += 1
            print(f"{self.name} is now {self.age} years old!")
        print(f"{self.name} is already dead!:(")
    
    def is_dead(self):
        if self.dead:            
            return True
        return False


# let's init a new human:
tilman = Human("Tilman", "01.01.1955")
# we cann acess properties and methods like this:
print(tilman.name)
print(tilman.age)
tilman.birthday()
print(tilman.age)
print(tilman.is_dead())
print(tilman.dead)

# we can modify properties:
tilman.dead = True
print(tilman.dead)

# finaly we can delete the object:
del tilman