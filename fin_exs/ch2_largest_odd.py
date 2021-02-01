print("Please input 10 integers:")
largest_odd = None
counter = 1
while counter <= 10:
    num = int(input(str(counter) + ":"))
    if (largest_odd == None and num % 2 != 0) or (num % 2 != 0 and num > largest_odd):
        largest_odd = num
    counter += 1
if largest_odd == None:
    print("You didn't give me any odd numbers!")
else:
    print("The largest odd number you input was " + str(largest_odd))