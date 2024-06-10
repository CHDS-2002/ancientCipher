# os - library for working with the console

import os

# Setting the font color of the console
os.system('COLOR B')


# get_password - function for creating a password
def get_password(number):
    return int(''.join([str(i) + str(j)
                        if not number % (i + j) and i < j else ''
                        for i in range(1, number)
                        for j in range(2, number)]))


# Generate a password
print('\nDATA ENTRY\n')
n = ''

while not n.isnumeric():
    n = input('Enter a number from 3 to 20: ')

    if n.isnumeric():
        if 3 <= int(n) <= 20:
            n = int(n)
            break
        else:
            n = ''

# Output the password
print('\nDATA OUTPUT')
print('\nPassword:', get_password(n), end='.\n\n')

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
