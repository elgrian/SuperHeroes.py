# .Find .Replace all [] brackets!!!!

import time
from sys import stdout
import random as ran
wordList = ["potato", "tomato", "ramen", "moana", "disney", "veil", "space", "bowie", "russia", "chair", "couch", "glasses", "orange", "apple", "carrot", "bread", "head", "beer", "pasta", "soda", "pizza", "eggs", "noodle", "coffee", "soup", "feet", "hands", "ears", "hoodie", "pencil", "sorbet", "juice", "fan", "pan", "cup", "boba", "cheese", "chair", "purse", "knife", "spoon", "steak", "netflix", "lemon", "grape", "weed", "phone", "tire", "liar", "bench", "thirst"] # Dictionary
alreadyGuessed = '' # alpha characters already chosen
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
        stringDisplay += ","
    print("Already guessed: " + ' '.join(alreadyGuessed))
    print(stringInput)

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
    # for char in losingString:
    #     stdout.write(char)
    #     stdout.flush()
    #     time.sleep(0.08)

else:
    print("Congratulations! You prevented the MoonMans death!")
    # winningString = ("Congratulations! You prevented the MoonMans death!")
    # for char in winningString:
    #     stdout.write(char)
    #     stdout.flush()
    #     time.sleep(0.08)
    #     break



# Global Variables
# WORD_LIST = ("potato", "tomato", "ramen", "moana", "disney", "veil", "space", "bowie", "russia", "chair", "couch", "glasses", "orange", "apple", "carrot", "bread", "head", "beer", "pasta", "soda", "pizza", "eggs", "noodle", "coffee", "soup", "feet", "hands", "ears", "hoodie", "pencil", "sorbet", "juice", "fan", "pan", "cup", "boba", "cheese", "chair", "purse", "knife", "spoon", "steak", "netflix", "lemon", "grape", "weed", "phone", "tire", "liar", "bench", "thirst")
# WORD = random.choice(WORD_LIST)
# ALLOWED = ("abcdefghijklmnopqrstuvwxyz")
#
# #Variables for game
#
# ## Create variable for IF guessed Variable == CharacterInWord (Turn the matching character(s) a specific color)
# guessedAlready = []
# state = 0
# timesWon = 0
# playedAlready = 0
#
#
# def main():
#     global guessedAlready, state, timesWon, playedAlready, WORD_LIST, WORD
#     setupMoonMan()
#     print("The word is " + str(len(WORD)) + "letters long.")
#     while (playAgain() == 1):
#         word =  random.choice(WORD_LIST)
#         guessAlready = []
#         playedAlready = 1
#         timesWon = 0
#         state = 0
#         while (guessedAlready() == 0 and state < 7):
#             # drawWord()
#             # drawMoonMan()
#             takeNewCharacter()
#         # drawMoonMan()
#         print("My word was " + WORD)
#
#
#  # Boolean :  1 == true, 0 == false
# def playAgain():
#     # 1 = int( 1 == 'true')
#     if (not playedAlready):
#         return True
#         True = input("\nDo you want to play again? (y/n)?")
#     while (True != "y" and True != "Y" and False != "n" and "N"):
#             True = input("\nDo you want to play again? (y/n)")
#     if (True.lower() == "y"):
#         return True
#     return False
#
#
#
# def inputNewLetter():
#     global state, timesWon
#     print("You have already guessed : ")
#     for character in guessAlready:
#         print(character, end=" ")
#     character = input("\n What will be your next guess? \n")
#     while (character in alreadyGuessed or character not in allowed):
#         if(len(character) > 1):
#             if (character.lower() == WORD.lower()):
#                 timesWon = 1
#                 break
#             else:
#                 print("\nOh no! \n BLAST OFF!!!")
#                 state = 7;
#                 break;
#         else:
#             if (character not in ALLOWED):
#                 char = input("Only lowercase characters are accepted, please try again.\n")
#             else:
#                 if (character not in ACCEPTABLE):
#                     character = input("Only lowercase characters are accepted, please try again.\n");
#                 else:
#                     character = input("Only lowercase characters are accepted, please try again.\n")
#                     guessed.append(letter);
#         if (character not in WORD):
#             state += 1;
#     return;
# #Create Words
#     def drawWord():
#         tempWord = "";
#         for c in WORD:
#             if (c in guessed):
#                 tempWord += c + " ";
#             else:
#                 tempWord += "_ ";
#                 newPrint(tempWord);
#     return;
