
movies = [
    "The Holy Grail", 1975, "Terry Jone @ Terry Gilliam", 91,
    ["Graham Chapman",
    ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]
]

print(movies[4][1][3]) ## Result: Eric Idle
print("----------")

print(movies)
print("----------")

for each_item in movies:
    print(each_item)
print("----------")

names = ['Michael', 'Terry']
print(isinstance(names, list))
# isinstance() BIF = check if a specific identifier holds data of a specific type
#True
print("----------")

num_names = len(names)
print(isinstance(num_names, list))
print("----------")

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)
