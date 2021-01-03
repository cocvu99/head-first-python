import pickle

with open('mydata.pickle', 'wb') as mysavedata:
    pickle.dump([1, 2, 'three'], mysavedata)

"""
The 'b' tells Python to open your data file in BINARY mode

To save your data, use "dump()"
"""

with open('mydata.pickle', 'rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)


"""
'a_list' = Assign your restored data to an identifier

"""

#Once your data is back in your program, you can treat it like any other data object
print(a_list)