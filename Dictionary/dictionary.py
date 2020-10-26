import time
fruit = {
    'orange': 'orange',
    'apple': 'red',
    'banana':'yellow',
    'pear':'green'
}
fruit_copy = dict(fruit) # OR --> fruit.copy()

print(f'Same values fruit == fruit_copy:  {fruit == fruit_copy}, BUT diff objects: fruit is fruit_copy: {fruit is fruit_copy}')

print(fruit_copy) #{'orange': 'orange', 'apple': 'red', 'banana': 'yellow', 'pear': 'green'}
print('apple' in fruit) #True , SAME AS ----> print('apple' in fruit.keys())
print('yellow' in fruit.values()) #True

fruit_copy.clear() # will empty the dictionary and will return None
print(fruit_copy) #{}

del fruit['pear'] #deletes this key/value entry, NOTHING IS RETURNED
for k in fruit: # SAME AS -------> for k in fruit.keys():
    print(k)
# orange
# apple
# banana
# pear WAS DELETED
print("=" * 40)

#====================================
keyValue = fruit.items()
print(keyValue) # dict_list containing tuples ---> dict_items([('orange', 'orange'), ('apple', 'red'), ('banana', 'yellow'), ('pear', 'green')])
tupleKeyValue = tuple(keyValue)
print(tupleKeyValue) # normal tuple ---> (('orange', 'orange'), ('apple', 'red'), ('banana', 'yellow'), ('pear', 'green'))
for snack in tupleKeyValue:
    k, v = snack
    print("{} is {}".format(k,v))


print(dict(keyValue))
print(dict(tupleKeyValue))

#{}.fromkeys()======== DEFAULT VALUES=============================================

new_user = {}.fromkeys(['name','score','email','profile'], 'unknown')
print(new_user)#{'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile': 'unknown'}

new_user2 = new_user.fromkeys("MIKE","defaultValue")
print(new_user2)# {'M': 'defaultValue', 'I': 'defaultValue', 'K': 'defaultValue', 'E': 'defaultValue'}

new_user3 = new_user.fromkeys("MIKE", [1,2,3,4,5])
print(new_user3)# {'M': [1, 2, 3, 4, 5], 'I': [1, 2, 3, 4, 5], 'K': [1, 2, 3, 4, 5], 'E': [1, 2, 3, 4, 5]}

#AS YOU CAN SEE, OBJECT.fromkeys(singleLETTERorLISTofKEYS,VALUE_FOR_KEYS) --> will always treat OBJECT as empty and will Return a new OBJECT.
#Also, an string/range() will be treated as a LIST of letters/keys.

#POPPING ITEMS ================================================================
print(new_user.pop('name'))#removes key/value and returns value
print(new_user)
print(new_user.popitem())#removes random key/value and returns tuple(key/value)
print(new_user)
#{}.update({}) --> Update/OVERRIDES keys and values in a dictionary with another set of keys value pairs.
first = {'name':'Michael', 'surname':'Zapata','age':'24'}
second = {'sports':'basketball', 'name':'mike'}
second.update(first)
print(second)#{'sports': 'basketball', 'name': 'Michael', 'surname': 'Zapata', 'age': '24'}



########################ORDER#######################################
print("ORDER "+"=" * 40)
ordered_keys = sorted(fruit.keys())# has type "list"
# ordered_keys = list(fruit.keys()) # normal "list"
# ordered_keys.sort()
for f in ordered_keys:
    print(f + '-' + fruit[f])
####################
#USING dics.values() is NOT as efficient as the method above or below
# create and sort the values dict_list first, then iterate through the values dict_list, we don't touch the keys.
ordered_values = sorted(fruit.values())# has type "list"
for value in ordered_values:
    print(value, end = ', ')
print('')
####################################################################
for snack in fruit:
    print(fruit[snack])
#####################################################################
#IF key is not in Dictionary, then myDict.get(key, return this default value if not present);
while True:
    dict_key = input('Enter the name of a fruit: ')
    if dict_key == 'quit':
        print('bye')
        break

    #LONG
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print("Color is : {} ".format(description))
    # else:
    #     print("We don't have a {}".format(dict_key))
    #SHORT
    description = fruit.get(dict_key, "We don't have a {}".format(dict_key))
    print(description)
########################################################################
#CONCATENATING STRING IS EXPENSIVE, SO USE .join() instead.
myList = ['a','b','c','d']

start = time.time()
newString = ''
for c in myList:
    newString += c + ', '
end = time.time()
print(newString, "Time taken: {:.10f}".format(end-start))

#better way ->
secondString = ', '.join(myList)
print(secondString)