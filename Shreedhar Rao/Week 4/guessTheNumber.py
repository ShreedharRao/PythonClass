# guess that number game
import random

num = random.randint(1, 9)
guess = False
counter = 0
while not guess:
    if counter < 2:
        userNum = int(input("Guess the number between 1 and 9: "))
        counter = counter + 1
        if userNum == num:
            print("You guess it right!")
            guess = True
            break
        elif userNum < num:
            print("Too low!")
        else:
            print("Too high!")
            break
        if counter >= 2:
            print("too many guesses")

if not guess:
    print('haha you lost')

