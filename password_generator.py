# Password Generator

# CODE

# Import relevant modules
import string
import random
import time
import tkinter as tk
from tkinter import messagebox

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
    #return password in the tkinter GUI
    #password_entry.config(text=f'{password}')
    password_entry.config(state='normal')
    password_entry.delete(0,'end')
    password_entry.insert(0,password)
    password_entry.config(state='readonly')

if __name__=='__main__':
    # Create a tkinter window
    root=tk.Tk()
    root.title('Secure Password Generator Tool')
    root.geometry('400x200')
    root.config(bg='navyblue')

    # Output field using Entry
    password_entry=tk.Entry(root,font=('consolas',12),justify='center')
    password_entry.config(bg='white',fg='black',state='readonly')
    password_entry.pack(pady=(50,10),padx=30,fill='x')

    # Create a button to generate password
    button=tk.Button(root,text='Generate Password',padx=5,pady=5,font=('consolas',12),command=create_password)
    button.pack(pady=(20,10))

    # Loop the tkinter window
    root.mainloop()
