# Author:   Jake in the Math Lab
# Date:     4/22/2022

class Monster:
    def __init__(self, name, health, power):
        self.name = name        # Name of the monster
        self.health = health    # Health Points (HP) 
        self.power = power      # (Attack) power, kinda like level
        self.moveset = []       # Moveset. Use addMove() to add more moves.
    
    def __str__(self):
        # This will allow a class to have a string representation 
        # when there is a print call to the instance.
        return f'{self.name} (HP {self.health}, Power {self.power})'
    
    def __repr__(self):
        # This will allow a class to have a string representation when the 
        # instance is within a data collection.
        return f'{self.name} (HP {self.health}, Power {self.power}, has {len(self.moveset)} moves)'
    
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