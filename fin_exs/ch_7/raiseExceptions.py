def findAnEven(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""
    value = None
    for i in L:
        if i % 2 == 0:
            value = i
            print(i)
            return i
    if value == None:
        raise ValueError("No even integers")

testList = [1, 3, 5, 7]
# testList = [1, 3, 4, 7]

findAnEven(testList)



