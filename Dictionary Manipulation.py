dict = { "a" :10 , "b" : 40, "c" : 80}
d = 10
if d in dict.values() :
    print(f"{d} exists in dictionary")
else :
    print(f"{d} does not exists in dictionary")

dict = { "a" : 10 , "b" : 40, "c" : 80}
min_key = min(dict , key=dict.get)
print("Minimum value:" , min_key)

dict = {"a" : 10 , "b" : 40 , "c" : 80}
keys_to_del = ["a" , "c"]
for i in keys_to_del :
    if i in dict :
        dict.pop(i)
print(dict)