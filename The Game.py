import random

for count in range (4) :
    randomDice = random.randrange (1,20)
print(randomDice)
if randomDice==(20):
    print ('critical hit')
if randomDice==(1):
    print('critical failure')
print ("action one: open the door or action two: flee")
import os.path
path='Opening Scenario.txt'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print('file does not exist')
import sys
userinput = 0
while userinput !=1:
    userinput = input('choose option 1: face your fear, to choose this option press 1, option 2:flee, to choose option 2 press 2, type your decision below:)')
    #convert to an integer
    try:
        userinput = int(userinput)
    except:
        print('incorrect, please put in a 1 or 2')
    if userinput == 1:
        print('on we go')
    if userinput == 2:
        print('game over')
        sys.exit()

import os.path
path='Description of the House.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
import sys
userinput = 0
while userinput !=1:
    userinput = input('choose option 1: continue towards the house, to choose this option, press 1;or option 2:flee, to choose option 2 press 2, type your decision below:)')
    #convert to an integer
    try:
        userinput = int(userinput)
    except:
        print('incorrect, please put in a 1 or 2')
    if userinput == 1:
        print('on we go')
    if userinput == 2:
        print('game over')
        sys.exit()
import os.path
path='Description of the kitchen.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
import sys
userinput = 0
while userinput !=3:
    userinput = input('choose (1) Search the kitchen,(2) Flee, (3) Go down the stairs')
    #convert to an integer
    try:
        userinput = int(userinput)
    except:
        print('incorrect, please put in a 1 or 2')
    if userinput == 1:
        print('you find nothing')
        sys.exit()
    if userinput == 2:
        print('game over')
        sys.exit()
    if userinput == 3:
        print('you go down the stairs into the basement')
import os.path
path='Basement.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
import sys
userinput = 0
while userinput !=3:
    userinput = input('choose (1) Right,(2) Flee, (3) Left')
    #convert to an integer
    try:
        userinput = int(userinput)
    except:
        print('incorrect, please put in a 1 or 2')
    if userinput == 1:
        print('you encounter Grilla unprepared and are killed by Grilla, Game Over')
        sys.exit()
    if userinput == 2:
        print('game over')
        sys.exit()
    if userinput == 3:
        print('you open the chest and find a key to a kabinet in the bedroom')
import os.path
path='Bedroom.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
import sys
userinput = 0
while userinput !=1:
    userinput = input(' option 1: open the cabinet,; option 2:flee, type your decision below:)')
    #convert to an integer
    try:
        userinput = int(userinput)
    except:
        print('incorrect, please put in a 1 or 2')
    if userinput == 1:
        print('You find a magical daggar you can use to defeate Grilla! Attached is a note.')
    if userinput == 2:
        print('game over')
        sys.exit()
import os.path
path='The note.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
import sys
userinput = 0
while userinput !=1:
    userinput = input(' option 1: take the daggar and face your fear; option 2:flee, , type your decision below:)')
    #convert to an integer
    try:
        userinput = int(userinput)
    except:
        print('incorrect, please put in a 1 or 2')
    if userinput == 1:
        print('You return to the basement to encounter Grilla')
    if userinput == 2:
        print('game over')
        sys.exit()
import os.path
path='The encounter.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
import sys
userinput = 0
while userinput !=1:
    userinput = input(' option 1: continue; option 2:flee, , type your decision below:)')
    #convert to an integer
    try:
        userinput = int(userinput)
    except:
        print('incorrect, please put in a 1 or 2')
    if userinput == 1:
        print('You find Grilla')
    if userinput == 2:
        print('game over')
        sys.exit()
import os.path
path='The fight.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
import random

for count in range (4) :
    randomDice = random.randrange (1,20)
print(randomDice)
if randomDice==(20):
    print ('critical hit')
if randomDice==(1):
    print('critical failure')
if randomDice >= 3:
    print ('you stunned Grilla!!')
if randomDice <= 3:
    print ('Game Over')
    sys.exit()
import sys
userinput = 0
while userinput !=1:
    userinput = input(' option 1: take the key to the observatory; option 2:flee, , type your decision below:)')
    #convert to an integer
    try:
        userinput = int(userinput)
    except:
        print('incorrect, please put in a 1 or 2')
    if userinput == 1:
        print('On We go to the observatory')
    if userinput == 2:
        print('game over')
        sys.exit()
import os.path
path='The observatory.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
import sys
userinput = 0
while userinput !=1:
    userinput = input(' Grilla is closing in, choose a chest: Chest 1; Chest 2; 3:Flee')
    #convert to an integer
    try:
        userinput = int(userinput)
    except:
        print('incorrect, please put in a 1 or 2')
    if userinput == 1:
        print('You open the chest to find a spear capable of defeating Grilla!')
    if userinput == 2:
        print('you find a moldy whopper from Burger King; Game over')
        sys.exit()
    if userinput == 3:
        print:('game over')
        sys.exit()
import os.path
path='The final battle.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
for count in range (4) :
    randomDice = random.randrange (1,20)
print(randomDice)
if randomDice==(20):
    print ('critical hit')
if randomDice==(1):
    print('critical failure')
if randomDice >= 5:
    print ('Congratualtions, You have defeated Grilla, the world can now be at peace all thanks to your heroics and bravery.')
if randomDice <= 5:
    print ('The spear breaks and you are defeated, Game Over')
    sys.exit()
import os.path
path='ending.txt.'
checkfile = os.path.isfile(path)
if checkfile == True:
    inputFile = open(path,'r')
    outputFile = inputFile.read()
    print(outputFile)
else:
    print ('file does not exist')
