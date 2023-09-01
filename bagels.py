#! python3
# bagels.py

import random, pyinputplus

class UserGuess:
    
    # Constructor
    def __init__(self, userGuessString:str):
        # Confirm that user guess is a three digit number.
        assert userGuessString.isdecimal(), "IsNotDecimal"
        assert len(userGuessString) == 3, "IsNotLengthThree"

        self.firstDigit = int(userGuessString[0])
        self.secondDigit = int(userGuessString[1])
        self.thirdDigit = int(userGuessString[2])

class SecretNumber:

    # Constructor: generate three random digits 0-9.
    def __init__(self):
        self.__firstDigit = random.randint(0,9)
        self.__secondDigit = random.randint(0,9)
        self.__thirdDigit = random.randint(0,9)

    # String Representation: put three digits together as string.
    def __string__(self):
        return f"{self.__firstDigit}{self.__secondDigit}{self.__thirdDigit}"
    
    # Compute clues to display and add to list.
    def getClues(self, userGuess:UserGuess):
        clues = []

        # check for clue in first digit.
        if userGuess.firstDigit == self.__firstDigit:
            clues.append("Fermi")
            isFirstDigitClued = True # so that program does not compute clues for this digit anymore
        elif userGuess.firstDigit in (self.__secondDigit, self.__thirdDigit):
            clues.append("Pico")
            isFirstDigitClued = True
        
        # check for clue in second digit.
        if userGuess.secondDigit == self.__secondDigit:
            clues.append("Fermi")
            isSecondDigitClued = True
        elif userGuess.secondDigit in (self.__firstDigit, self.__thirdDigit):
            clues.append("Pico")
            isSecondDigitClued = True

        # check for clue in third digit.
        if userGuess.thirdDigit == self.__thirdDigit:
            clues.append("Fermi")
        elif userGuess.thirdDigit in (self.__firstDigit, self.__secondDigit):
            clues.append("Pico")

        # put Bagels clue if there is no clue in list.
        if len(clues) == 0:
            clues.append("Bagels")

        return clues
        


def main():
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
        while True:
            print(f"Guess #{guessCount}")
            try:
                currentUserGuess = UserGuess(input("> "))
                break
            except AssertionError:
                print("Please enter a three digit number.")

        # Compute clues.
        clues = currentSecretNumber.getClues(currentUserGuess)

        # Check for game was won.
        if clues.count("Fermi") == 3:
            print("You got it!")
            playAgain = pyinputplus.inputYesNo(prompt="Do you want to play again? (yes or no)\n> ", limit=3)
            if playAgain == "yes":
                guessCount = 0
                print("")
                continue
            break
        
        # Display clues.
        clueDisplayString = ""
        for clue in clues:
            clueDisplayString += f"{clue} "
        print(clueDisplayString)

        # Break loop if game is over.
        if guessCount > 10:
            print("You didn't get it!")
            playAgain = pyinputplus.inputYesNo(prompt="Do you want to try again? (yes or no)\n> ", limit=3)
            
            if playAgain == "yes":
                guessCount = 0
                print("")
                continue
            break

main()