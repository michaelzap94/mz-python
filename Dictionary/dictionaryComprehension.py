str1 = 'ABC'
str2 = '123'
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo) # {'A': '1', 'B': '2', 'C': '3'}


instructor = {'name': 'colt', 'city':'san francisco', 'color':'purple'}
yelling = {k.upper() : v.upper() for k,v in instructor.items()}
print(yelling) # {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}

myIfAtTheEndTest = {k.upper() : v.upper() for k,v in instructor.items() if (k is 'color')}
print(myIfAtTheEndTest)

num_list=range(1,20)
new_dict = {n: ('even' if(n % 2 == 0) else 'odd') for n in num_list}
print(new_dict) # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even', 11: 'odd', 12: 'even', 13: 'odd', 14: 'even', 15: 'odd', 16: 'even', 17: 'odd', 18: 'even', 19: 'odd'}


