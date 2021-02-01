#adds up the digits in string "s" without using any methods that
#haven't been covered in the book

s = "1.23,2.4,13.123"
total = 0
current = 0
dec = False

for d in s:
    if d == ",":
        total = total + current
        current = 0
        dec = False
    elif d == ".":
        dec = 1
    elif dec == False:
        current = 10*current + int(d)
    elif dec:
        current = current + int(d)/10**dec
        dec += 1

print(total+current)
    
