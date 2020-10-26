class Animal:
    cool = True # Class attribute

    def make_sound(self, sound):
        print(f"this animal says {sound}")


# Cat class inherits from Animal
class Cat(Animal):
    pass

# Make a new cat instance
blue = Cat()

# Because of inheritance, a Cat has access to:
blue.make_sound("Meow") # "this animal says Meow"
print(blue.cool) # True
print(Animal.cool) # True
print(Cat.cool)# True, as Cat inherits both Class and Instance attributes/methods from Animal

#blue is both a Cat and Animal (and base object)
print(isinstance(blue, Cat)) # True
print(isinstance(blue, Animal)) # True
print(isinstance(blue, object)) # True

#=======================================
