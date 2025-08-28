n = 1
while n <=10 :
    print(n)
    n +=1

n = int(input("Enter number:"))
i = 2
while i <= n:
    print(i)
    i += 2

n = int(input("Enter number:"))
i = 1
while i <= n:
    print(i)
    i += 2

n = int(input("Enter your number:"))
i = 1
while i <= 10 :
    print(f"{n} * {i}  , {n * i} ")
    i += 1

n = int(input("Enter your number:"))
for num in range(2 , n +1) :
    prime = True
    for i in range(2 , num) :
        if num % i == 0:
            prime = False
            break
        if prime :
            print(num)