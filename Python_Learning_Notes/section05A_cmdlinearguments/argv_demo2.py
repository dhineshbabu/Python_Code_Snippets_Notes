from sys import argv

print("The Number of command line arguments: ", len(argv))
print("The List of command line arguments: ", argv)
print("List of command line arguments are : ")

for x in argv:
    print(x)
