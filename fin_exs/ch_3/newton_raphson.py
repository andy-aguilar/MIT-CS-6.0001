epsilon = 0.01
k = 25
guess = k/2.0
guessCount = 0

while abs(guess*guess -k) >= epsilon:
    guessCount +=1
    guess = guess - (((guess**2) - k)/(2*guess))
print("Guess Count = " + str(guessCount))
print('Square root of', k, 'is about', guess)