

import re

def main():
    instructions = 'Enter an IP address. Enter quit to stop: '

    my_input = input(instructions)

    while my_input != 'quit':
        ips = containsIPAddress(my_input)
        if len(ips) == 0:
            print('No IP found.')
        else:
            for ip in ips:
                print(ip)
        my_input = input(instructions)
    
    print('Have a nice day!')

def containsIPAddress(inString):
    pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    ips = pattern.findall(inString)
    return ips

main()