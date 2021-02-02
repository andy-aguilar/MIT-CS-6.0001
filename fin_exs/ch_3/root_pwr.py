user_input = int(input("Please enter an integer:"))
root = None
pwr = None

for x in range(1, user_input):
    for y in range(2, 6):
        if x**y == user_input:
            root = x
            pwr = y
            break

if root:
    print("Root = " + str(root) + " Pwr = " + str(pwr))
else:
    print("nope, nope, nope")
