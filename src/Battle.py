from HumanHero import HumanHero
from HumanVillain import HumanVillain
from Villain import Villain
from Hero import Hero


class Battle:
    def __init__(self, hero, villain):
        self.hero = hero
        self.villain = villain

    def fight(self):
        heroStats = self.hero.getStats() + self.hero.getBonus()
        villainStats = self.villain.getStats() + self.villain.getBonus()
        if heroStats > villainStats:
            self.hero.wins += 1
            self.villain.losses += 1
        elif villainStats > heroStats:
            self.villain.wins += 1
            self.hero.losses += 1
        else:
            self.hero.ties += 1
            self.villain.ties += 1

