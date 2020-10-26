# A User class with both a class attribute
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

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


class Moderator(User):
    total_mods = 0
    #Class methods - python passes not the instance of the class 'self' BUT the actual class, and calls it 'cls'
    #Class methods are methods( with the @classmethod decorator) that are not concerned with instances, but the class itself.
    @classmethod
    def display_active_mods(cls):
        print(cls) # <class '__main__.User'>
        return f"There are currently {cls.total_mods} active Moderators."

    def __init__(self, first, last, age, community):
        super().__init__(first,last,age)
        self.community = community
        Moderator.total_mods += 1

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"


jasmine = Moderator("Jasmine", "oconner", 61, 'piano')
print(jasmine.full_name(), jasmine.community) # Jasmine oconner piano

# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user2.initials())
# print(user1.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# user1.say_hi()

print('Active Users:',User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print('Active Users:',User.display_active_users())


print('Active Moderators:',Moderator.display_active_mods())










