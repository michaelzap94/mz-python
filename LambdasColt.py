def square(num):
    return num * num

square2 =  lambda num: num * num # a lambda is an anonymous function automatically returned. like square2 = (num)=> num*num in js, NOTICE if {} you need return: square2 = (num)=> { return num*num }

print(square(9))
print(square.__name__) # square

print (square2(9))
print(square2.__name__) # <lambda>

# lambda IS SUPPOSED to be anonymous, and run in one line of code.