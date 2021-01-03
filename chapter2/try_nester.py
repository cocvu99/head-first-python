import nester

cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
print("----------")

movies = [ "The Holy Grail", 1975, "Terry Jones & Terry Gilliam",
91,["Graham Chapman", ["Michael Palin",
"John Cleese", "Terry Gilliam", "Eric Idle",
"Terry Jones"]]]

nester.print_lol(movies, 2)

names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]
print("----------")

#nester.print_lol(names, -9)
nester.print_lol(names, True)

"""
NOTE: thuc hien cac cau lenh sau truoc khi thay doi package
*python3 = c:python/python.exe

python3 setup.py sdist 
python3 setup.py install

python3 setup.py sdist register upload // OR
twine upload dist/*

"""