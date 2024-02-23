# Map
# Looping without a loop
# Maps function calls to a collection of items
# map(func, iterables)

# Basic usage - count len

people = ['Paul', 'Bryan', 'Jin', 'Yoshimitsu']

# old way of counting
counts = []
for x in people:
    counts.append(len(x))
print(f'Old way: {counts}')

# modern way
print(f'Mapped: {list(map(len, people))}')

# More Complex Usage
firstnames = ('Apple', 'chocolate', 'Fudge', 'Pizza')
lastnames = ('Pie', 'Cake', 'Brownies')

def merg(a, b):
    return a +' '+ b

x = map(merg, firstnames, lastnames)
print(x)
print(list(x))

# Multiple functions - Combine functions
# Call multiple functions in one map call

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def do_all(func, num):
    return func(num[0], num[1])

f = (add, sub, mul, div)

v = [[5,3]]
n = list(v) * len(f)
print(f'f: {f}, {n}')

final_op = map(do_all, f, n)

print(final_op)
print(list(final_op))