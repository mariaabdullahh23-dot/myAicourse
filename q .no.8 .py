cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp
    print("Profit")
    print(f"Amount is {profit}")
elif sp < cp:
    loss = cp - sp
    print("Loss")
    print(f"Amount is {loss}")
else:
    print("No Profit, No Loss")
