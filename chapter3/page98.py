import os

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print('  said:  ')
            print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

"""
This version uses another "try"
statement to handle File I/O errors
"""