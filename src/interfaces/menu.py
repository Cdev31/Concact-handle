from colorama import Fore
import questionary
from .login import login

def menu():
    print("Manejador de contactos")
    menu = questionary.select(
        "Your choose",
        choices=[
            "Login",
            "contacts",
            "exit"
        ]
    ).ask()

    if menu == 'Login':
        login()
        
    