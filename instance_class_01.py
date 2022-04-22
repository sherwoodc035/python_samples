# Author: Jake from the Math Lab

# Define a class

class InstanceClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

# Add instances to list

instanceList = []
instance1 = InstanceClass("Jake", 366)
instanceList.append(instance1)
instance2 = InstanceClass("Katelyn", 9)
instanceList.append(instance2)

# Display information for instances in list

for inst in instanceList:
    # 'inst' is referencing the instance of the class that stored from the previous code
    print(inst) # This will print all the attributes from that list or some gnarly stuff you may have not seen before.
    # NOT USEFUL for our intended purposes.
    print("") # Line break
    
    # Method 1: Use proper get_() functions that were created in class to access the specific attribute
    print("Method 1:")
    x1 = inst.getX()
    y1 = inst.getY()
    print("X = ", x1 , " Y = ", y1)
    print("")
    
    # Method 2: Use the attribute name from the class definition
    print("Method 2:")
    x2 = inst.x
    y2 = inst.y
    print("X = ", x2 , " Y = ", y2)
    print("")

# End of Program