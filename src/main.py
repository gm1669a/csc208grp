class Main:
    def __init__(self):
        self.powerList = []
        self.heroList = []
        self.villainList = []
        self.battleList = []

    def main(self):
        self.powerList = BattleRoyale().getPowerList()
        self.heroList = BattleRoyale().getHeroList()
        self.villainList = BattleRoyale().getVillainList()
        self.battleList = BattleRoyale().getBattleList()
        for battle in self.battleList:
            battle.fight()
        for hero in self.heroList:
            print(hero.name, 'wins:', hero.wins, 'losses:', hero.losses, 'ties:', hero.ties)
        for villain in self.villainList:
            print(villain.name, 'wins:', villain.wins, 'losses:', villain.losses, 'ties:', villain.ties)
        for character in self.powerList:
            print(character.name, 'wins:', character.wins, 'losses:', character.losses, 'ties:', character.ties)