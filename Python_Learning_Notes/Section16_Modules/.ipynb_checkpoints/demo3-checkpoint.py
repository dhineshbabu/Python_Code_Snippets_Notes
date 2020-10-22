import os

"""
This is a documentation string and can be accessed by modulename.__doc__
"""
print(__doc__)

# to print the file name
print("File name: ",__file__)

# print file absolute path
print("File full absolute path: ", os.path.abspath(__file__))

# print directory name

print("Directory name: ", os.path.dirname(os.path.abspath(__file__)))