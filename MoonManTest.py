import time
from sys import stdout
import random as ran
wordList = ["potato", "tomato", "ramen", "moana", "disney", "veil", "space", "bowie", "russia", "chair", "couch", "glasses", "orange", "apple", "carrot", "bread", "head", "beer", "pasta", "soda", "pizza", "eggs", "noodle", "coffee", "soup", "feet", "hands", "ears", "hoodie", "pencil", "sorbet", "juice", "fan", "pan", "cup", "boba", "cheese", "chair", "purse", "knife", "spoon", "steak", "netflix", "lemon", "grape", "weed", "phone", "tire", "liar", "bench", "thirst"] # Dictionary
alreadyGuessed = [] # alpha characters already chosen
word = wordList[ran.randint(0, len(wordList) - 1)]
stringSplit = list(word) # Creates an array from the characters within the string.
stringInput = ["_"] * len(stringSplit)



def guessInput():
    printWordHint = ("The word is " + str(len(word)) + " letters long.\n")
     # Causes a delay inbetween each character being printed so that is creates the illusion of typing.
    for char in printWordHint:
        stdout.write(char)
        stdout.flush()
        time.sleep(0.03)
    return input("Guess a letter!")

### Have had issues getting this loop to print only the final array
# Prints the guessed characters, without the array brackets.
def changeCharToUnderScore(eachLetter):
    stringDisplay = ""
    for x in eachLetter:
        stringDisplay += x
        stringDisplay += " "
    print("Already guessed: " + ', '.join(alreadyGuessed))
    print (stringDisplay)

#replace hidden character from "_" to the "alpha character".
def replaceUnderScore(split, userInp):
    inputForGuess = guessInput()
    alreadyGuessed.append(inputForGuess)
    changedCharacter = True
    for x in range(len(split)):
        if inputForGuess == split[x]:
            userInp[x] = stringSplit[x]
            changedCharacter = False
    return(userInp, changedCharacter)

# Starting Game and calling Functions
changeCharToUnderScore(stringInput)
amtOfWrongGuesses = 0
correctGuess = True


while(not("_" not in stringInput or amtOfWrongGuesses >= 7)):
    stringInput, correctGuess = replaceUnderScore(stringSplit, stringInput)
    if not correctGuess:
        amtOfWrongGuesses += 1
        print("Oh no, that is not in this word!")
    changeCharToUnderScore(stringInput)
if(amtOfWrongGuesses >= 7):
    print("Blast Off! You LOSE! \nThe correct word was " + word)


else:
    print("Congratulations! You prevented the MoonMans death!")
    # winningString = ("Congratulations! You prevented the MoonMans death!")
