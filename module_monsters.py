# Author: Jake in the Math Lab

class Monster:
    def __init__(self, name, health, power, moveset):
        self.name = name        # Name of the monster
        self.health = health    # Health Points (HP) 
        self.power = power      # (Attack) power, kinda like level
        self.moveset = []  # Moveset. Pass in as a list
    
    # Get definitions
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getPower(self):
        return self.power
    def getMoveset(self):
        return self.moveset
    
    # Set definitions
    def setName(self, newName):
        self.name = newName
    def setHealth(self, newHealth):
        self.health = newHealth
    def setPower(self, newPower):
        self.power = newPower
    
    # Create and add to moveset
    def addMove(self, newMove):
        self.moveset.append(newMove)

# --------------
# End of program
# --------------