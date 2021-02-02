x = -27

neg = 1

if x < 0:
    x = x*-1
    neg = -1

epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2

while abs(ans**3 - x) >= epsilon:
    print('low = ', low, 'high = ', high, 'ans = ', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

ans = ans * neg

print('numGuesses =', numGuesses)
print(ans, 'is close to the square root of', x)