h=34
height=5.3
name="maria"
print("height", height)
print ( "h" ,h)
print ("name",name) 
print(type(h))
print(type(height))
print(type(name))
int =print(int(input("please input int")))
sum=h+height
print("sum" ,sum)
sub=h-height
print("sub",sub )
product=h*height
print("product",product)
divide=h/height
print("divide",divide)
if h > height :
    print ("greater")
elif h<height :
    print("less")
else:
    print("equal")
if h > height or h <height:
    print("less")
else:
     print("equal")
intro="my name is maria.i am studing AIfull stack in Netskill"
print("intro",intro)
print(type(intro))
part= intro[11:16] 
print(part)
for i in intro :
    if i == "m":
       break 
    print(i)
for i in intro :
    if i == "m":
     continue
    print(i)  


myint = 0
while myint < 3:
    print(myint)
    myint=myint +1

print(len(intro))
print(intro[: : -1])
