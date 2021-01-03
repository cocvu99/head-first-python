import os

#check where I am working? 
print(os.getcwd())

# Two following lines code is add
man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            
            # Remove unwanted whitespace
            line_spoken = line_spoken.strip()
                
            #Condition    
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')

try:
    with open('man_data.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('other_data.txt', 'w') as other_file:
        print(other, file=other_file)

except IOError as err:
    print('File Error.' + str(err))

with open('man_data.txt', 'w') as man_file, open ('other_data.txt', 'w') as other_file:
    print(man, file=man_file)
    print(other, file=other_file)

"""
NOTE: No need to close your file, 
because "with" does that for you
"""