# Test Class

class Person:
    # Weak Private - convention to use the variable only inside the class. Private to the class
    _name = 'No Name'

    def setName(self, name):
        self._name = name
        print(self._name)
       