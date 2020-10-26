locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
             1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
             2: {"N": 5, "Q": 0},
             3: {"W": 1, "Q": 0},
             4: {"N": 1, "W": 2, "Q": 0},
             5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

vocabulary = { "QUIT":  "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST":  "E",
               "WEST":  "W",
               "ROAD": "1",
               "HILL": "2",
               "BUILDING": "3",
               "VALLEY": "4",
               "FOREST": "5"
            }



loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    # NOT EFFICIENT( concatenating strings in Python is very consuming)
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                print('vocabulary is: {}, and word(key)is {}'.format(vocabulary, word))
                direction = vocabulary[word]
                break
    print('direction: ', direction)
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

############CONVINE DICTIONARIES#########
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit, please",
       "lime": "NEWNEWNEW"}

print('='*60)
# create a new dictionary
# # veg and fruit will NOT be modified.
newJoin = dict(veg, **fruit) # || dict(**veg, **fruit) THE ONE ON THE LEFT HAS HIGHER PRIORITY.
print(newJoin)
print(veg)
print(fruit)

#UPDATING RETURNS None
# create a new dictionary
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg) # append AND update this 'nice_and_nasty' dictionary using 'veg' properties.
print(nice_and_nasty)
# veg and fruit will NOT be modified.
print(veg)
print(fruit)

print(veg.update(fruit)) # returns None
print(veg) # will modify veg

print(fruit.update(veg)) # returns None
print(fruit) # will modify fruit