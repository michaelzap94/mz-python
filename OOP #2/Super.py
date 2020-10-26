# Inheritance Example Using Super()
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Pet(Animal):
    # def __init(self, name, breed, toy, species):
    #     self.name = name
    #     self.species = species
    def __init__(self, name, breed, toy, species = "Pet"):
        # Animal.__init__(self,name,species) # BETTER TO USE BELOW METHOD:
        super().__init__(name, species) # Call init on parent class
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")



blue = Pet("Blue","Scottish Fold", "String", "Dog")
red = Pet("Red", "Spanish Fold", "Not String")

print(blue) # Blue is a Pet
blue.play() # Blue plays with String

print(red)
red.play()

# OUR "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy