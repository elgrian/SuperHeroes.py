#delay
import time
from sys import stdout
#Asking for guided input
name = input("What is your name? : ")
place = input("Where is somewhere that you would enjoy living? : ")
verb1 = input("What would be a painful type of injury? (i.e: Cut, Broken, Burnt) : ")
bodyPart = input("What body part would suck to hurt? : ")
medicine = input("What is a cure all medicine? :  ")
crush = input("Who is a celebrity/person you know, who you have crush on? : ")
adjective1 = input("Give me an adjective to describe a person? : ")
favShow = input("What is your favorite TV Show/ Movie? : ")
favFood = input("What is your favoite snack food? :  \n \n")

#Completed input Print
print("Now that I have all the information I need, here is the story I have created for you! \n \n")
time.sleep(0.2)


# Story
madLibs = """{} was a beginner programmer who moved to {}. When they got there, they ended up getting a huge {} on their {}. Needless to say, it wasn't pleasant and they hurried
quickly to the E.R. Like always, the E.R. was full and the wait would be hours. They took their care into their own hands and just decided to take some {}. The {} didn't work
and they blacked out from the pain. When they came to, {} was standing over them. Their {} was too much to handle and {} quickly ran away in embarassment and hid in their
apartment. {} eventually began watching {} to release some stress, while eating {}. They ended up choking on the {} and unfortunately met their demise. \n \n""".format(name, place, verb1, bodyPart,
medicine, medicine, crush, adjective1, name, name, favShow, favFood, favFood)

# print each character with a delay, flush
for char in madLibs:
    stdout.write(char)
    stdout.flush()
    time.sleep(0.04)

print ("The End!")
