# Often ignored
# _Single
# __Double
# __Before
# After__
# __Both__

# Skipping
for _ in range(5):
    print('hello')

from person import *

#_Before  (single) - Weak Private. Internal user only for the defined class
p = Person()
p.setName("dhinesh")
print(f'Modifying outside the class. So it is weak private')
p._name = "New Name"
print(f'Modified name : {p._name}')

#__Before  (Double) -  Internal use only, avoid conflict in subclass
# and tells python to rewrite the name (Mangling)
p = Person()
p.work()
# p.__think() #AttributeError: 'Person' object has no attribute '__think'
# c = Child()
# c.testDouble() #AttributeError: 'Child' object has no attribute '_Child__think'

# After (Any)
# Helps and used in scenario where to avoid naming conflicts with key words
class_ = Person()
print(class_)

# Before and After
# These are all special in python like the init and main function
p = Person()
p.__call__()
