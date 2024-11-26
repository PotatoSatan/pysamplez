import random
import sys

randomizedNumber = random.randint(1, 5)

print(f"Guess the number that I'm thinking from 1 to 5. You have 3 chances.")

for guesses in range(1, 8):
    try:
        print('Take a guess.')
        guess = int(input())
    except (NameError, ValueError):
        print('Not an integer, try again.')
        continue
    if guess > randomizedNumber:
        print('Your guess is too high.')
    elif guess < randomizedNumber:
        print('Your guess is too low.')
    else:
        break
1
if guess == randomizedNumber:
    print('yes it' + str(randomizedNumber) + ' ' + str(guesses))
else:
    print('gago kaba')