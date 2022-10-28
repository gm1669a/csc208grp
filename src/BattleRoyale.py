import csv
class Hero:
    def __init__(self, name, intelligence, strength, speed, durability, power, combat):
        self.name = name
        self.intelligence = intelligence
        self.strength = strength
        self.speed = speed
        self.durability = durability
        self.power = power
        self.combat = combat

    def getStats(self):
        threeStatsSum = self.intelligence + self.speed + self.power
        return threeStatsSum

    def getBonus(self):
        bonus = 0
        strength = int(self.strength)
        combat = int(self.combat)
        if strength >= 85:
            bonus += 5
        if combat >= 90:
            bonus += 10
        return bonus
class Villian:
    def __init__(self, name, intelligence, strength, speed, durability, power, combat):
        self.name = name
        self.intelligence = intelligence
        self.strength = strength
        self.speed = speed
        self.durability = durability
        self.power = power
        self.combat = combat

    def getStats(self):
        threeStatsSum = self.strength + self.durability + self.combat
        return threeStatsSum

    def getBonus(self):
        bonus = 0
        speed = int(self.speed)
        intelligence = int(self.intelligence)
        if speed >= 85:
            bonus += 5
        if intelligence >= 90:
            bonus += 10
        return bonus

with open('../SuperpowerDataset.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    powerList = []

    for row in reader:
      #  print(row['Alignment'], row['Name'])
        if row['Alignment'] == 'good':
            oName = Hero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            oName.getBonus()
        elif row['Alignment'] == 'bad':
            oName = Villian(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            oName.getBonus()
        else:
            oName = Hero(row['Name'], row['Intelligence'], row['Strength'], row['Speed'], row['Durability'], row['Power'], row['Combat'])
            oName.getBonus()