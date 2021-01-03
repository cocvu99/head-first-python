import pickle
import nester

man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':')
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
            else:
                pass
        except ValueError:
            pass

    data.close()
except IOError:
    print('The datafile is missing!')

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, file=man_file)
        pickle.dump(other, file=other_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

new_man = []

try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)

except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

nester.print_lol(new_man)
print("----------")

#Dong dau tien cua doan van
print(new_man[0])
print("----------")

#Dong cuoi cung cua doan van
print(new_man[-1])
print("----------")

