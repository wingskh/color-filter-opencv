import os

def clear_console():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Linux/OS X
        os.system('clear')