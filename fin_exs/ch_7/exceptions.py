def sumDigits(s):
    sList = list(s)
    total = 0
    for str in sList:
        try:
            total += int(str)
        except:
            total += 0
    return total

print(sumDigits("a2b3c"))





