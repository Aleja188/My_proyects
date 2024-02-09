import os

def clear():
    sistema_operativo = os.name

    if sistema_operativo == 'posix':  # Linux y macOS
        os.system('clear')
    elif sistema_operativo == 'nt':  # Windows
        os.system('cls')

