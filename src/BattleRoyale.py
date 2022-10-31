import csv

from HumanHero import HumanHero
from HumanVillain import HumanVillain
from Villain import Villain
from Hero import Hero



with open('../SuperpowerDataset.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    powerList = []

    for row in reader:
      #  print(row['Alignment'], row['Name'])
        if row['Alignment'] == 'good':
            if row['Race'] == 'Human':
                oName = HumanHero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
                oName.getBonus()
            else:
                oName = Hero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
                oName.getBonus()
            powerList.append(oName)
        elif row['Alignment'] == 'bad':
            if row['Race'] == 'Human':
                oName = HumanVillain(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'],
                                  row['Power'], row['Combat'])
                oName.getBonus()
            else:
                oName = Villain(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
                oName.getBonus()
            powerList.append(oName)
        else:
            if row['Race'] == 'Human':
                oName = HumanHero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
                oName.getBonus()
            else:
                oName = Hero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
                oName.getBonus()
            powerList.append(oName)


#   FOR DEBUGGING
#   for character in powerList:
#       print(character.name, ',', character.getBonus())
