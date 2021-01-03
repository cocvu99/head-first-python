import os

os.getcwd()
print(os.getcwd()) 
#Result is E:\Github\head-first-python\chapter3

"""
os.chdir('../HeadFirstPython/chapter3')
os.getcwd()
"""
data = open('sketch.txt')
print(data.readline(), end='')
print(data.readline(), end='')

data.seek(0)
"""
seek() method to return to the start of the line 
And yes, you can use "tell()" with Python's files, too
"""

for each_line in data:
    print(each_line, end='')

data.close()