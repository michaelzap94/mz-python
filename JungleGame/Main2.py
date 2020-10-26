from HelloWorld.JungleGame.Land import Land
from HelloWorld.JungleGame.Sea import Sea
from HelloWorld.JungleGame.Air import Air
from HelloWorld.JungleGame.Air import Animal

class Main2():
    tiger = Land('tiger')
    eagle = Air('eagle')
    shark = Sea('shark')

    setAlive = {tiger,eagle,shark}
    deadAnimals = set()
    while(len(deadAnimals)<len(setAlive)-1):
        tiger.life = tiger.life - (eagle.specificAttack['punch']+shark.specificAttack['punch'])
        eagle.life = eagle.life - (tiger.specificAttack['punch']+shark.specificAttack['punch'])
        shark.life = shark.life - (eagle.specificAttack['punch']+tiger.specificAttack['punch'])

        print('DEAD ANIMALS:', list(map(lambda x: x.specificAttack['name'], list(deadAnimals))))

        difference = setAlive.difference(deadAnimals) # Gets only elements on the left SET not including intersection
        for aliveAnimal in difference:
            print(f'Live left for {aliveAnimal.specificAttack["name"]:} {aliveAnimal.life}')
            if(Animal.getLife(aliveAnimal) <= 0):
                deadAnimals.add(aliveAnimal)


    else:
        difference = list(setAlive.difference(deadAnimals)) # Gets only elements on the left SET not including intersection
        print(f'Winner is {difference[0].specificAttack["name"]}')

