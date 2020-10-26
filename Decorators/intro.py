#NO DECORATOR
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        return fn()
    return wrapper

def greet():
    print("My name is mike")


greet = be_polite(greet)
greet()

#DECORATOR

@be_polite
def greet_dec():
    print("My name is Michael")

greet_dec()

