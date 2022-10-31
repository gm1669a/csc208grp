from Hero import Hero


class HumanHero(Hero):

    def __init__(self, name, intelligence, strength, speed, durability, power, combat):
        super().__init__(name, intelligence, strength, speed, durability, power, combat)

    def getBonus(self):
        return super().getBonus() - 5

    def __str__(self):
        return 'I am a Human Hero'