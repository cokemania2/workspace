minBurger = 2000
minBeverage = 2000
for i in range (3) :
    a = int(input())
    if a < minBurger :
        minBurger = a
for i in range (2) :
    b = int(input())
    if b < minBeverage :
        minBeverage = b
print(minBurger + minBeverage - 50)
