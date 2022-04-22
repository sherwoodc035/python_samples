# Author:   Jake in the Math Lab
# Date:     4/22/2022

class Move:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description
    
    def __str__(self):
        # This will allow a class to have a string representation 
        # when there is a print call to the instance.
        return f'{self.name} ({self.type}): {self.description}'
    
    def __repr__(self):
        # This will allow a class to have a string representation when the 
        # instance is within a data collection.
        return f'{self.name} ({self.type}): {self.description}'
    
    # Get definitions
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getDesc(self):
        return self.description
    
    # Set definitions
    def setName(self, newName):
        self.name = newName
    def setType(self, newType):
        self.type = newType
    def setDesc(self, newDescription):
        self.description = newDescription

# --------------
# End of program
# --------------