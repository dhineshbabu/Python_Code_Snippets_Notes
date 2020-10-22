from sys import argv

args = argv[1:]
sum=0

for x in args:
    sum = sum + int(x)

print('The sum: ', sum)
