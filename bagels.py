#! python3
# bagels.py

import random

class SecretNumber:

    # Constructor: generate three random digits 0-9.
    def __init__(self):
        self.__firstDigit = random.randint(0,9)
        self.__secondDigit = random.randint(0,9)
        self.__thirdDigit = random.randint(0,9)

    # String Representation: put three digits together as string.
    def __string__(self):
        return f"{self.__firstDigit}{self.__secondDigit}{self.__thirdDigit}"
    
    def getClues(self, firstDigit, secondDigit, thirdDigit)
    


# Display starting game information.
print("I am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:")
print("When I say 'Pico' that means one digit is correct but in the wrong position.")
print("When I say 'Fermi' that means one digit is correct and in the right position.")
print("When I say 'Bagels' that means no digit is correct.")

# Generate random three digit number.
currentSecretNumber = SecretNumber()
print("I have thought up a number.")

print("You have 10 guesses to get it.")

# Main game loop.
guessCount = 0
while True:
    guessCount += 1 # Track number of guesses.

    # Accept user guess.
    print(f"Guess #{guessCount}")
    userGuess = input("> ")

    # Compute clues.


    # Display clues.