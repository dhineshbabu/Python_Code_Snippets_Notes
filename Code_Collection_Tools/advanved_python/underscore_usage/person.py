# Test Class

class Person:
    # Weak Private - convention to use the variable only inside the class. Private to the class
    _name = 'No Name'

    def setName(self, name):
        self._name = name
        print(self._name)
       
    # Strong Private
    def __think(self):
        print('Thinking to my self')

    def work(self):
        self.__think()

    # Before and After
    def __init__(self) -> None:
        print('Inside Constructor')

    def __call__(self):
        print('Call someone')


class Child(Person):
    def testDouble(self):
        self.__think(self)