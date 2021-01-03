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

print(man)
print(other)