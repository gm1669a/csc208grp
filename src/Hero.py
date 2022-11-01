from SuperPower import SuperPower
class Hero(SuperPower):

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