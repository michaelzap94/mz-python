# Instance Attributes  and Methods use the self and are attached to each specific Object
# Class Attributes and Class Methods do not use the self and are shared by all instances of a class and the class itself.

class User:
    #Class attribute
    active_users = 0

    #Class methods - python passes not the instance of the class 'self' BUT the actual class, and calls it 'cls'
    #Class methods are methods( with the @classmethod decorator) that are not concerned with instances, but the class itself.
    @classmethod
    def display_active_users(cls):
        print(cls) # <class '__main__.User'>
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_string):
        first,last,age = data_string.split(',')
        #User(first,last,age) instead use:
        return cls(first,last,age) # returns the new User.

    def __init__(self, first, last, age): # SELF is the specific instance of the Class
        self.first = first
        self.last = last
        self.age = age
        self._msgPrivate = 'this is private'
        self.__msgSuperPrivate = 'this is SUPER private'
        print(f"A new user {self.first} has been made")
        #active_users += 1 # will not work
        User.active_users +=1

    #LIKE THE toString() method in JAVA. will print this string when printing a User instance.
    def __repr__(self):
        return f"{self.first} is {self.age}"

    def full_name(self):
        return self.first + ' ' + self.last

    def logout(self):
        User.active_users -=1
        print(f"{self.first} has logged out")


user1 = User('Joe','Jackel',456)
user2 = User('Blanca','Sur',156)
print(type(user1)) # <class '__main__.User'>
print(type(user2)) # <class '__main__.User'>

print(user1.first) # Joe

print(user1._msgPrivate)
#print(user1.__msgSuperPrivate) # WILL NOT BE POSSIBLE
print(dir(user1)) # ['_User__msgSuperPrivate', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_msgPrivate', 'age', 'last', 'name']
print(user1._User__msgSuperPrivate) # this is SUPER private

print(user1.full_name())


# Class Methods - NOT commonly used. - They don't rely on any information that is particular to any instance.
print(User.display_active_users()) # There are currently 2 active users.

user3 = User.from_string("Tom,Jones,89") # A new user Tom has been made
print(user3) # without the __repr__ <__main__.User object at 0x00DE5690> BUT Tom is 89 WITH the __repr__

# Class attribute access
print(User.active_users) #3
user1.logout() # Joe has logged out
print(User.active_users) #2


# Another class with a class attribute, used for validation purposes
class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']
    staticAttr = 'Static'
    staticValue = 'I am static'

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
        print(Pet.staticAttr) # Static
        #Access Class attribute as an Instance attribute - valid
        print(self.staticAttr) # Static
        #UPDATE Instance attribute self.staticAttr , it will not update the Class attribute staticAttr
        self.staticAttr = 'Not Static'
        print(self.staticAttr) # Not Static
        print(Pet.staticAttr) # Static

    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

print(id(cat.allowed) == id(dog.allowed) == id(Pet.allowed)) # True

print(Pet.staticValue) # I am static
print(cat.staticValue) # I am static

cat.staticValue = 'Michael is static'
print(cat.staticValue) # 'Michael is static'
print(dog.staticValue) # 'I am static'
print(Pet.staticValue) # 'I am static'

print(Pet.__dict__)


