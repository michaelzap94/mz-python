nums = list(range(2,11,2))
print(nums) # [2, 4, 6, 8, 10]

"""Map: will iterate through a list and will return whatever it is defined in the function. --> map(function,list)"""
# passing lambda, notice any function can be passed. eg: map(int,list)
doubles = map(lambda x: x*2, nums)
print(doubles) # <map object at 0x00E8EA90>
doubles_list = list(doubles)
print(doubles_list) # [4, 8, 12, 16, 20]

# using list comprehension instead of Map function
doubles_list_comprehension = [x * 2 for x in nums]
print(doubles_list_comprehension) # [4, 8, 12, 16, 20]

"""Filter: take a list and filters out particular items, it will only return what satisfies the condition"""
mList = [1,2,3,4]
evens = list(filter(lambda x : (x%2 == 0), mList)) # return x only if true., where x is an element in mList
print(evens) # [2, 4]

"""any(iterable) True if any is true OR False if empty ||| all(iterable) True if ALL true OR True if empty"""
print(any([0,0,0])) # False
print(any([0,2,3])) # True

print(all([1,2,3])) # True
print(all([0,2,3])) # False

#======================================
users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
# sorted() default is Alphapetical ASC. to do DESC, you need to pass another arg reverse=True.
# To sort by length of keys
print(sorted(users, key=len))

# To sort users by their username
sorted(users,key=lambda user: user['username'])

# Finding our most active users...
# Sort users by number of tweets, descending
sorted(users,key=lambda user: len(user["tweets"]), reverse=True)

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
sorted(songs, key=lambda s: s['playcount'])

#=============== min(iterable, [key])/max(iterable, [key])========================================================
names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
min(len(name) for name in names) # 3

# find the longest name itself
print(max(names, key=lambda n:len(n))) #Ollivander
# OR
print(max(names, key=len))#Ollivander

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA

print(dir(names))

#====================zip=======================================
print('zip '+'='*40)

x = zip('hello','homie')
print(list(x)) # [('h', 'h'), ('e', 'o'), ('l', 'm'), ('l', 'i'), ('o', 'e')]

y = zip('hellosssss','homie')
print(list(y)) # [('h', 'h'), ('e', 'o'), ('l', 'm'), ('l', 'i'), ('o', 'e')] STOPS as soon as ANY ITERABLE RUNS OUT

packed = [(1,2,3),(1,2,3),(1,2,3)]
z = zip(*packed)
print(list(z))# [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
#=========zip advanced===============================================================

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']
# returns dict with {student:highest score} USING LIST COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
mZip = zip(students, midterms, finals) #
#print(list(mZip))# [('dan', 80, 98), ('ang', 91, 89), ('kate', 78, 53)] , if this line is executed, mZip will be empty.
final_grades = {t[0]:max(t[1], t[2]) for t in mZip}
print(final_grades)# {'dan': 98, 'ang': 91, 'kate': 78}
#SHORTER
final_gradesOWN = {name: (max(midterms[i],finals[i])) for i,name in enumerate(students) }
print(final_gradesOWN)

# returns dict with {student:highest score} USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades_map_lambda_zip = zip(students, map(lambda grades: max(grades),zip(midterms, finals)))
final_grades_map_lambda_dict= dict(final_grades_map_lambda_zip)
print(final_grades_map_lambda_dict)# {'dan': 98, 'ang': 91, 'kate': 78}

#MYOWN
newZip = zip(students,finals, midterms)
OWN_lambda = map(lambda newZip: (newZip[0],(max(newZip[1],newZip[2]))), newZip)
print('OWN_lambda ', dict(OWN_lambda))

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0]+pair[1])/2),
            zip(midterms, finals)
        )
    )
)


