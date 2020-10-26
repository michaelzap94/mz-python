class Human:
    def __init__(self, f,l, age):
        self.first = f
        self.last = l
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    #    NORMAL GETTERS AND SETTERS

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = 0

    #    DECORATORS GETTERS AND SETTERS

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >0:
            self._age = value
        else:
            raise ValueError("age can't be negative!")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first , self.last = name.split(' ')



jane = Human("Jane", "Goodall", -9)
print(jane.age) # Error, as there's no property age, but _age which is supposed to be private

#using Getters and Setters
print(jane.get_age()) # 9
jane.set_age(45)
print(jane.get_age()) # 9

# USING @property and @age.setter DECORATOR
print(jane.age) # 45
jane.age = 56
print(jane.age) # 56

# any
print(jane.full_name)
jane.full_name = "Tim Muchn"
print(jane.full_name)
print(jane.__dict__) # {'first': 'Tim', 'last': 'Muchn', '_age': 56}

#===================================================================================