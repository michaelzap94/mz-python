class Animal():
    animalCount = 0
    habitatAttackMultiplier = {'Land': 10, 'Air': 5, 'Sea': 4}
    habitatSuperpowerLimit = {'Land': 80, 'Air': 70, 'Sea': 60}
    attackSet = {'punch','kick','bite','combo','superPower'}
    attackPointsPercentage = (2,3,1,4,6)

    if __name__ == "__main__":

        #NOT USED##############################
        superPowerChargeLimitDefault = 50
        superPowerChargeLimitDict = {}.fromkeys(['superPowerLimit'],superPowerChargeLimitDefault)
        attackDict = dict(zip(attackSet, attackPointsPercentage))
        mergedDict = dict(**attackDict,**superPowerChargeLimitDict)
        print('General AttackDictReady', mergedDict)
        #######################################

     #print('General AttackDictReady', mergedDict) WILL NOT WORK as it is OUTSIDE the scope


    def __init__(self, habitat, animalName):
        self.habitat = habitat
        self.animalName = animalName
        Animal.animalCount = Animal.animalCount + 1
        self.specificAttack = self.getSpecificDictAttack(habitat, animalName)

    @classmethod
    def getLife(cls, animal):
        return animal.life;

    @classmethod
    def howManyInJungle(cls):
        #Animal.animalCount OR cls.animalCount, as cls ---> refers to the Class variables.
        return f'There are {cls.animalCount} {"animals" if(Animal.animalCount>1) else "animal"} in the jungle.'

    def getSpecificDictAttack(self, habitat, animalName):
        habitat = habitat if(isinstance(habitat, str)) else habitat.__name__
        dictToReturn = {'name': animalName.capitalize(), 'habitat': habitat}
        dictAttackPoints = dict(zip(Animal.attackSet, [x * Animal.habitatAttackMultiplier[habitat] for x in Animal.attackPointsPercentage]))
        dictSuperpowerLimit = {'superPowerLimit': Animal.habitatSuperpowerLimit[habitat]}
        #{}.update({}) --> Update/OVERRIDES keys and values in a dictionary with another set of keys value pairs.
        # OR
        return dict(**dictToReturn, **dictAttackPoints, **dictSuperpowerLimit)

    def __repr__(self):
        return f'''Animal {self.animalName.capitalize()} from {self.habitat} \nAttackSpecs: {self.specificAttack}'''

def main():
    landAnimal = Animal('Land', 'tiger')
    print(landAnimal)

    airAnimal = Animal('Air', 'eagle')
    print(airAnimal)

    seaAnimal = Animal('Sea', 'shark')
    print(seaAnimal)

    print(Animal.howManyInJungle())



if __name__ == "__main__":
    main()
    print(f"Class {__name__} Invoked directly ===================")
else:
    print(f"Class {__name__} Imported ===========================")
