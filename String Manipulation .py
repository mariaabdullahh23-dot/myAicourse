a = input("Enter value:")
first = a[0]
midindex = len(a) // 2
middle = a[midindex]
last = a[-1]
result = first + middle + last
print(result)

b = input("Enter value:")
for i in set(b) :
    print(i ,  ":" , b.count(i))

c = input("Enter value:")
rev_c = c[: : -1]
print(rev_c)

d = input("Enter value:")
d_split = d.split("-")
print("After splitting:" , d_split)

e = input("Enter value:")
pretty = "" 
for i in e :
    if i.isalnum() or i == "" :
     pretty += i 
print("pretty string:" , pretty) 