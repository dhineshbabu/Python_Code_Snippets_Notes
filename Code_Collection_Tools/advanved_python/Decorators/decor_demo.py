# Decorators

# Function that takes some additional functionality and returns it

# Basic Decorator
# In this example, we will change the execution order

def test_decorator(func):
    print('before')
    func()
    print('after')


@test_decorator
def do_stuff():
    print('Doing stuff')

# Real time decorator

def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner # returning inner function


@makeBold
def printName():
    print('Optimus Prime')

printName()

# Decorators with parameters

def numCheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('can not divide by Zero')
                return False
            return True

        print(f'{o} is not a number')
        return False

    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x, y)
    return inner

@numCheck
def divide(a,b):
    print(a/b)

divide(100,3)
divide(100, 0)
divide(100, 'cat')

# Decorator Chaining

def outline(func):
    def inner(*args, **kwargs):
        print('~'*20)
        func(*args, **kwargs)
        print('+'*20)
    return inner


def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        for x in args:
            print(f'arg = {x}')
        for k, v in kwargs.items():
            print(f'Key = {k} Value = {v}')
    return inner

@outline
@list_items
def display(msg):
    print(msg)


display('hello world')

@outline
@list_items
def birthday(name='', age=0):
    print(f'Happy birthday {name} , you are {age} years old')

birthday(name='optimius', age=200)