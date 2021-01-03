import sys

"""
The Scholar's Corner:

Standard Output: The default place where your code writes its 
data when the “print()” BIF is used. This is typically the screen. 
In Python, standard output is referred to as “sys.stdout” and 
is importable from the Standard Library’s “sys” module

The following example:
"""

sys.stdout.write(str(99) + '\n')
sys.stdout.write('Hello World')

#Result on screen: 99 \n Hello World
