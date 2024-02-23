# pickle
# Serializing Objects
# Saving and Loading objects and their states
# Python data types, and top level classes

import pickle
from typing import Collection

# simple decorator for printing good representation

def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('-'*20)
    return inner

# Simple class
class Cat:
    def __init__(self, name, age, info) -> None:
        self._name = name
        self._age = age
        self._info = info

    @outline
    def display(self, msg=''):
        print(msg)
        print(f'{self._name} is a {self._age} years old')
        for k , v in self._info.items():
            print(f'{k} = {v}')

othello = Cat('Othello', 15, dict(color='Balck',weight=15,loves='eating'))
othello.display('Testing')

#Serializing
sc = pickle.dumps(othello)
print(sc)

with open('cat.txt', 'wb') as f:
    pickle.dump(othello, f)

# Deserializing

mycat = pickle.loads(sc)
print('From String:')
mycat.display('from String')

with open('cat.txt', 'rb') as f:
    diskcat = pickle.load(f)

diskcat.display('From Disk:')

print(mycat)
print(diskcat)