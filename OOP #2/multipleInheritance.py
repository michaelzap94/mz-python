class Aquatic:
    def __init__(self,name):
        print("AQUATIC INIT!")
        self.name = name
    def swim(self):
        return f"{self.name} is swimming"
    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self,name):
        print("AMBULATORY INIT!")
        self.name = name
    def walk(self):
        return f"{self.name} is walking"
    def greet(self):
        return f"I am {self.name} of the land!"

#THE FIRST CLASS WOULD HAVE PREFERENCE (from the MRO) AND ITS METHODS WILL BE USED in case another super class also has the same methods
# THE __init__ will call the FIRST CLASS(Ambulatory) only, as it has preference (from the MRO), HOWEVER. this class will still inherit the methods from SECOND CLASS(Aquatic)
class Penguin(Ambulatory, Aquatic):
    def __init__(self,name):
        print("PENGUIN INIT!")
        super().__init__(name=name)

        # IF we want to execute both __init__
        # Ambulatory.__init__(self,name=name)
        # Aquatic.__init__(self, name=name)

#=============================================================================
#MRO - ORDER in which classes have preference., 3 ways to find out:
print(Penguin.__mro__) # (<class '__main__.Penguin'>, <class '__main__.Ambulatory'>, <class '__main__.Aquatic'>, <class 'object'>)
print(Penguin.mro()) # [<class '__main__.Penguin'>, <class '__main__.Ambulatory'>, <class '__main__.Aquatic'>, <class 'object'>]
help(Penguin)
# Method resolution order:
# |      Penguin
# |      Ambulatory
# |      Aquatic
# |      builtins.object

#=============================================================================

jaws = Aquatic("Jaws")#AQUATIC INIT!
lassie = Ambulatory("Lassie")#AMBULATORY INIT!
captain_cook = Penguin("Captain Cook") #PENGUIN INIT!
                                       #AMBULATORY INIT!

print(captain_cook.swim())#Captain Cook is swimming
print(captain_cook.walk())#Captain Cook is walking
print(captain_cook.greet())#I am Captain Cook of the land!
print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}") #True
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}") #True
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}") #True



# jaws.swim() # 'Jaws is swimming'
# jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
# jaws.greet() # 'I am Jaws of the sea!'

# lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
# lassie.walk() # 'Lassie is walking'
# lassie.greet() # 'I am Lassie of the land!'

# captain_cook.swim() # 'Captain Cook is swimming'
# captain_cook.walk() # 'Captain Cook is walking'
# captain_cook.greet() ##I am Captain Cook of the land!
