# Author:   Jake in the Math Lab
# Date:     4/22/2022

from module_moves import *
from module_monsters import *
import pprint as pp

def introduction():
    print('------------------------------------------------')
    print('Welcome to your Monster Roster where you can add')
    print('  and modify your monster team!')
    print('------------------------------------------------')

def instruct_manage_roster():
    print('----------Managing your Monster Roster----------')
    print('Options (pick one): ROSTER, MONSTER, REMOVE, EXIT')

def conclusion():
    print('------------------------------------------------')
    print('Thank you for using the Monster Roster for your')
    print('  monster management needs! Have a good day!')
    print('------------------------------------------------')

def main():
    introduction() # Let's the user know the program is running
    
    roster = [] # Initialize roster
    while True:
        # Loop for creating monsters
        x = input('Would you like to create a monster (Y/N)?: ').casefold()

        if x == 'n':
            # The user is done making monsters. Exit the loop.
            print('----------Finished creating monsters---------')
            print('') # Line break
            break
        elif x == 'y':
            # The user is creating a monster.
            print('----------Create a Monster---------')
            name = input('What would you like to name your monster?: ')
            health = input('How much health points (HP) does the monster have?: ')
            power = input('What is the monster\'s attacking power or level?: ')
            monster = Monster(name, health, power)
            
            # The user is adding moves for the monster
            while True:
                # Define a set of moves for the monster
                y = input('Would you like to add a move for the monster (Y/N)?: ').casefold()
                if y == 'n':
                    # User is done adding moves. Exit the loop.
                    break
                elif y == 'y':
                    # The user is making a move for the monster
                    name = input('What is the name of the move?: ')
                    type = input('Type of move?: ')
                    description = input('Description for the move: ')
                    move = Move(name, type, description)
                    monster.addMove(move)
                    print('Move has been added!\n')
                else:
                    # The command entered did not match the previous if statements. Re-prompt.
                    print('You have entered an invalid command. Please type Y or N.')
                    print('') # Line break

            # The user is done adding moves. Add the monster to the roster.
            roster.append(monster)
            print('Monster added to the roster!')
            print('') # Line break
        else:
            # The command entered did not match the previous if statements. Re-prompt.
            print('You have entered an invalid command. Please type Y or N.')
            print('') # Line break
    
    
    while True:
        # User can now manage the roster
        instruct_manage_roster()
        x = input('What would you like to do? ').casefold()

        if x == 'exit':
            # The user is done managing their roster. Exit the loop.
            break
        elif x == 'roster':
            # The user wants to view the roster
            pp.pprint(roster)
        elif x == 'monster':
            # The user wants to view info about a monster in the roster
            y = input('Which monster do you want to see? Please enter a name: ').casefold()

            found = None # Sets a flag for if the monster can be found
            for monster in roster:
                # Search for the monster's name in the roster
                if y == monster.getName().casefold():
                    # Reserves the monster since it has been found and exit the loop
                    found = monster 
                    break
            if found == None:
                # If the monster was not found, display a message
                print('The monster was not found in the roster.')
                print('') # Line break
            else:
                # Monster was found, display it's information
                print(found)
                print('Moveset:')
                pp.pprint(found.getMoveset())
                print('') # Line break
        elif x == 'remove':
                # User wants to remove a monster from the roster
                # Display the roster first
                pp.pprint(roster)
                y = input('Which monster do you want to remove? Please enter a name: ')

                found = None # Sets a flag for if the monster can be found
                for monster in roster:
                    # Search for the monster's name in the roster
                    if y == monster.getName().casefold():
                        # Reserves the monster since it has been found and exit the loop
                        found = monster 
                        break
                if found == None:
                    # If the monster was not found, display a message
                    print('The monster was not found in the roster.')
                    print('') # Line break
                else:
                    # Monster was found, display it's information
                    roster.remove(found)
                    print(f'{found.getName()} was removed from the roster! Goodbye {found.getName()}!')
                    print('') # Line break

        else:
            # The command entered did not match the previous if statements. Re-prompt.
            print('You have entered an invalid command. Please follow the instructions.')
            print('') # Line break

    conclusion()

main() # Call main

# --------------
# End of program
# --------------