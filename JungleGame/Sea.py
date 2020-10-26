from HelloWorld.JungleGame.Animal import Animal
class Sea(Animal):
    #className = __name__;

    def __init__(self, animalName):
        self.animalName = animalName
        self._life = 60
        super().__init__(self.__class__.__name__,animalName)

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, currentLife):
        self._life = currentLife



def main():
    tiger = Sea('shark')
    print(tiger)
if __name__ == "__main__":
    main()
    print(f"Class {__name__} Invoked directly ===================")
else:
    print(f"Class {__name__} Imported ===========================")