print('---------------------------------')

print(f'Running main.py-------- Running {__name__}----------')

import module1

print('Importing module again') # Nothing will happen here since it is already added to sys modules cache
# we can check it in globals()

import module1

print('---------------------------------')
