s = "1.23,2.4,13.123"
total = 0
current = 0
dec = False

# I know that the easy way to do this is to split at the commas
# then convert to floats and then add but I wanted to use only 
# what we've learned so far we haven't even learned functions 
# yet so I couldn't even create a split function

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
    
