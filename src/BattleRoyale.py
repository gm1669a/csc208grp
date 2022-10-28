import csv
from Villain import Villain
from Hero import Hero



with open('../SuperpowerDataset.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    powerList = []

    for row in reader:
      #  print(row['Alignment'], row['Name'])
        if row['Alignment'] == 'good':
            oName = Hero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            oName.getBonus()
        elif row['Alignment'] == 'bad':
            oName = Villain(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            oName.getBonus()
        else:
            oName = Hero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            oName.getBonus()