class Villain:
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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def intelligence(self):
        return self.__intelligence

    @intelligence.setter
    def intelligence(self, newIntelligence):
        try:
            newIntelligence = int(newIntelligence)
        except(TypeError, ValueError):
            raise TypeError('New intelligence is an invalid type. Please enter an integer.')
        if (newIntelligence < 0) or (newIntelligence > 105):
            raise ValueError('New intelligence must be between 0 and 105.')
        self.__intelligence = newIntelligence

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, newStrength):
        try:
            newStrength = int(newStrength)
        except(TypeError, ValueError):
            raise TypeError('New strength is an invalid type. Please enter an integer.')
        if (newStrength < 0) or (newStrength > 105):
            raise ValueError('New strength must be between 0 and 105.')
        self.__strength = newStrength

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, newSpeed):
        try:
            newSpeed = int(newSpeed)
        except(TypeError, ValueError):
            raise TypeError('New speed is an invalid type. Please enter an integer.')
        if (newSpeed < 0) or (newSpeed > 105):
            raise ValueError('New speed must be between 0 and 105.')
        self.__speed = newSpeed

    @property
    def durability(self):
        return self.__durability

    @durability.setter
    def durability(self, newDurability):
        try:
            newDurability = int(newDurability)
        except(TypeError, ValueError):
            raise TypeError('New durability is an invalid type. Please enter an integer.')
        if (newDurability < 0) or (newDurability > 105):
            raise ValueError('New durability must be between 0 and 105.')
        self.__durability = newDurability

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, newPower):
        try:
            newPower = int(newPower)
        except(TypeError, ValueError):
            raise TypeError('New power is an invalid type. Please enter an integer.')
        if (newPower < 0) or (newPower > 105):
            raise ValueError('New power must be between 0 and 105.')
        self.__power = newPower

    @property
    def combat(self):
        return self.__combat

    @combat.setter
    def combat(self, newCombat):
        try:
            newCombat = int(newCombat)
        except(TypeError, ValueError):
            raise TypeError('New combat is an invalid type. Please enter an integer.')
        if (newCombat < 0) or (newCombat > 105):
            raise ValueError('New combat must be between 0 and 105.')
        self.__combat = newCombat