list = ["maria" , "AI full stack" , 2025] 
list.reverse()
print("Reverse list:" , list)

n = [1, 2, 3, 4, 5]
square = []
for i in n:
    square.append(i**2)
print("Square of list:" , square)

list = ["maria" , "" , "AI fullstack" , 2025] 
while "" in list:
    list.remove("")
print(list)

list = ["maria" , "AI full stack" , 2025] 
a = list.index("maria") 
list.insert(a + 2 , "Arfa")
print(list)

list = ["maria" , "AI full stack" , 2025] 
if "maria" in list: 
    a = list.index("maria") 
    list[a] = "Arfa"
print(list)