
cast = ["Cleese", "Palin", 'Jones', "Idle"]
print(cast)

print(len(cast)) ### Result: 4
print("----------")
print(cast[1]) ### Result Palin
print("----------")

cast.append("Gilliam") ### Chen them 'Gilliam' vao cuoi danh sach
print(cast)
print("----------")

cast.pop() ## Remove data from the END OF THE LIST
print(cast)
print("----------")

cast.extend(["Gilliam", "Chapman"])
print(cast)
print("----------")

cast.remove("Chapman")
print(cast)

cast.insert(0, "Chapman")
print(cast)
#['Chapman', 'Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']