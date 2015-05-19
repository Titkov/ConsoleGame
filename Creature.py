from abc import ABCMeta, abstractmethod


class Creature(metaclass=ABCMeta):

    def __init__(self, damage, defense, health, mana, stamina, critChance, attackRad):
        self.damage = damage
        self.defense = defense
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.critChance = critChance
        self.attackRad = attackRad
        self.coords = (0, 0)

    def getDamage(self):
        return self.damage

    def getDefense(self):
        return self.damage

    def getHealth(self):
        return self.health

    def getMana(self):
        return self.mana

    def getStamina(self):
        return self.stamina

    def getCritChance(self):
        return self.critChance

    def getCoords(self):
        return self.coords

    def setDamage(self, damage):
        self.damage = damage

    def setDefense(self, defense):
        self.defense = defense

    def setHealth(self, health):
        self.health = health

    def setMana(self, mana):
        self.mana = mana

    def setStamina(self, stamina):
        self.stamina = stamina

    def setCritChance(self, critChance):
        self.critChance = critChance

    def setCoords(self, coords):
        self.coords = coords

    @abstractmethod
    def Move(self, prevCoords, newCoords):
        pass

    @abstractmethod
    def Attack(self, prevCoords, newCoords):
        pass
