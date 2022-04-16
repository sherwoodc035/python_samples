# Repeats request for input until sentinel value (e.g. "quit") is entered

def prompt():
    # Define a function known as the Prompt. Instructs the user on what to do.
    # Inputs:   None
    # Outputs:  String (from user input)
    instruction = 'Please enter something or enter "quit" to end the program: '
    return input(instruction)

def main():
    while (True): # Enters an infinite loop until False or 'break' is encountered

        my_input = prompt() # This is the start of a post-test loop

        print('  You entered:', my_input) # Print input from user

        # Check input for "quit". Continue to loop until "quit" is entered
        if my_input == 'quit':
            break
    # End of while loop

    print('  Have a nice day!') # End of program message

main()