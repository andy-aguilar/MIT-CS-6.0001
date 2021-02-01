x = int(input("Enter a number x:"))
y = int(input("Enter a number y:"))
z = int(input("Enter a number z:"))

if x%2 != 0 and (y % 2 == 0 or x > y) and (z % 2 == 0 or x > z):
    print("x is the largest odd #")
elif y%2 != 0 and (x % 2 == 0 or y > x) and (z % 2 == 0 or y > z):
    print("y is the largest odd #")
elif z%2 != 0 and (x % 2 == 0 or z > x) and (y % 2 == 0 or z > y):
    print("z is the largest odd #")
else:
    print("no odd numbers")


