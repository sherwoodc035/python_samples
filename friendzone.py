"""
0 = Friendzoned
1 = Accomplice
2 = Dating
"""

def relationshipStatus(i):
    if i == 0:
        return "Friendzoned"
    elif i == 1:
        return "Accomplice"
    else:
        return "Dating"

x = int(input("What is my status? "))
print(relationshipStatus(x))