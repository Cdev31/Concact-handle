import questionary
from colorama import Fore


def login():

    print(f"{Fore.RED}You must write your correct email and password")

    email = questionary.text("Your email: ").ask()

    password = questionary.password("Your password: ").ask()