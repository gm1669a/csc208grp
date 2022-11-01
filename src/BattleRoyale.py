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
            powerList.append(oName)
        elif row['Alignment'] == 'bad':
            if row['Race'] == 'Human':
                oName = HumanVillain(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'],
                                     row['Power'], row['Combat'])
                oName.getBonus()
            else:
                oName = Villain(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'],
                                row['Power'], row['Combat'])
                oName.getBonus()
            powerList.append(oName)
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

for i in range(len(powerList)):
    for j in range(len(powerList)):
        if i != j:
            if powerList[i].getStats() + powerList[i].getBonus() > powerList[j].getStats() + powerList[j].getBonus():
                powerList[i].wins += 1
                powerList[j].losses += 1
            elif powerList[i].getStats() + powerList[i].getBonus() < powerList[j].getStats() + powerList[j].getBonus():
                powerList[i].losses += 1
                powerList[j].wins += 1
            else:
                powerList[i].ties += 1
                powerList[j].ties += 1

for i in range(len(powerList)):
    print(powerList[i].name, powerList[i].wins, powerList[i].losses, powerList[i].ties)

