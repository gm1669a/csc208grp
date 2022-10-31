from src.Battle import *
from src.BattleRoyale import *

class Main:
    def __init__(self):
        self.battle = Battle()
        self.battleRoyale = BattleRoyale()

    def main(self):
        self.battleRoyale.battleRoyale()