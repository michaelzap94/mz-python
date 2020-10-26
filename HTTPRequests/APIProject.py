import requests
from random import randint
myInput = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/"
res2 = requests.get(
    url + 'search?',
    headers = {
        "Accept":"application/json"
    },
    params={
        "term" : myInput,
        "limit": 10
    })

result = res2.json()
jsonDataWQuery = result['results']
noOfResults = len(jsonDataWQuery)
if(noOfResults>0):
    randIndex = randint(0,noOfResults-1)
    print(f"I've got {len(jsonDataWQuery)} jokes about {myInput}. Here's one: \n {jsonDataWQuery[randIndex]['joke']}")
else:
    print(f"Sorry, I don't have any jokes about {myInput}! Please try again.")

