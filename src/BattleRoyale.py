import csv

from HumanHero import HumanHero
from HumanVillain import HumanVillain
from Villain import Villain
from Hero import *

with open('../SuperpowerDataset.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    powerList = []

    for row in reader:
        if row['Alignment'] == 'good':
            if row['Race'] == 'Human':
                oName = HumanHero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'],
                                  row['Power'], row['Combat'])
                oName.getBonus()
            else:
                oName = Hero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'],
                             row['Power'], row['Combat'])
                oName.getBonus()
        elif row['Alignment'] == 'bad':
            if row['Race'] == 'Human':
                oName = HumanVillain(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'],
                                     row['Power'], row['Combat'])
                oName.getBonus()
            else:
                oName = Villain(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'],
                                row['Power'], row['Combat'])
                oName.getBonus()
        else:
            if row['Race'] == 'Human':
                oName = HumanHero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'],
                                  row['Power'], row['Combat'])
                oName.getBonus()
            else:
                oName = Hero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'],
                             row['Power'], row['Combat'])
                oName.getBonus()
        powerList.append(oName)

# WE NEED TO MAKE SURE CHARACTERS FIGHT IN EACH MATCH ONCE
fighters = powerList.copy()
for i in range(len(powerList)):
    for j in range(len(powerList)):
        if i != j:
            if powerList[i].getStats() + powerList[i].getBonus() > powerList[j].getStats() + powerList[j].getBonus():
                powerList[i].wins += 1
            elif powerList[i].getStats() + powerList[i].getBonus() < powerList[j].getStats() + powerList[j].getBonus():
                powerList[i].losses += 1
            else:
                powerList[i].ties += 1

# REPORT FOR INDIVIDUAL CHARACTERS
for i in range(len(powerList)):
    print(powerList[i].name, 'Wins:', powerList[i].wins, 'Losses:', powerList[i].losses, 'Ties:', powerList[i].ties)

# REPORT TO SHOW WHICH CHARACTER HAD THE BEST RECORD
winningScore = powerList[0].getScore()
winningCharacter = powerList[0].name
losingScore = powerList[0].getScore()
losingCharacter = powerList[0].name
for character in powerList:
    if character.getScore() > winningScore:
        winningScore = character.getScore()
        winningCharacter = character.name
    if character.getScore() < losingScore:
        losingScore = character.getScore()
        losingCharacter = character.name
print('The character with the best record was', winningCharacter, 'with a score of', str(winningScore))
print('The character with the worst record was', losingCharacter, 'with a score of', str(losingScore))



