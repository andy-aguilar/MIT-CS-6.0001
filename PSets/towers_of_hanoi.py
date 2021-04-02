# def printMove(fr, to):
#     print('move from ' + str(fr) + ' to ' + str(to))


counter = 0

def Towers(n, fr, to, spare):
    global counter
    if n == 1:
        counter += 1
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


Towers(29, 1, 2, 3)
print(counter)
