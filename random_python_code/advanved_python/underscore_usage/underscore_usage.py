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