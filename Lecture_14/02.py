age=int(input("Enter your age"))
day=str(input("Enter day"))

price=12 if age>=18 else 8

if(day=="Wednesday"):
    price = price-2

print("ticket price:",price)