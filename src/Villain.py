from SuperPower import SuperPower
class Villain(SuperPower):

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