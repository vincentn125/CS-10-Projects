# The things that we need in this program are:
# Computer generates a random number from 0-100
# User input
# Compare the user input to the random number generated
# if randomNum == userGuess then it is a match
# if randomNum > userGuess then tell user to go HIGHER
# if randomNum < userGuess then tell user to go LOWER
# ONLY loop around user input to the comparisons

import random
randomNum = random.randint(0, 100)

# just testing print(randomNum)

userTries = 0
userGuess = 0

while userGuess != randomNum:
    userGuess = int(input("Guess a number from 0-100: "))
    if userGuess > randomNum:
        print("Guess lower...")
    else:
        print("Guess higher...")

    userTries += 1

print("Congrats! You guessed the correct number! The number is: ", randomNum)
print("You took", userTries, "tries!\n")
