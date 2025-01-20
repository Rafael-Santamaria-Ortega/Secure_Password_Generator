# Password Generator

# CODE

# Import relevant modules
import string
import random
import sys
import time

# Define a function to create passwords for repeatability
def create_password():

    # Make various lists to store the different type of characters
    upper=list(string.ascii_uppercase)
    lower=list(string.ascii_lowercase)
    numb=list(string.digits)
    punct=list(string.punctuation)

    # Shuffle each type of character using random module 
    random.shuffle(upper)
    random.shuffle(lower)
    random.shuffle(numb)
    random.shuffle(punct)

    # Create an empty list with result
    result=[]

    # Populate result with 20% of each character type
    for i in range(4):
        result.append(upper[i])
        result.append(lower[i])
        result.append(numb[i])
        result.append(punct[i])

    # Shuffle result again for randomness
    random.shuffle(result)

    # Create password object
    password=''.join(result)

    # Return password on screen
    return print(f'Here is your strong password: {password}')

# define function to ask if user wants to create another password
def ask():
    q=input('Do you want to create another password (y/n)?: ')
    
    # If so, call function again. If not, terminate the program
    if q=='y':
        run=True
    elif q=='n':
        run=False
        sys.exit('Closing program.')
    else:
        print('Please answer "y" or "n"')
        q=input('Do you want to create another password (y/n)?: ')
        if q=='y':
            run=True
        else:
            run=False

if __name__=='__main__':
    time.sleep(1)
    print('This is a Python-based secure password generator tool made by Rafael Santamaria')
    print('-------------------------------------------------------------------------------')
    time.sleep(1)

    # Create a while loop to keep the app going until user decides to close it
    run=True

    while run==True:
        # Call the function to create strong password
        create_password()
        # Call the function to ask if more passwords are desired
        print('--------------------------------------------------------------------------------')
        ask()