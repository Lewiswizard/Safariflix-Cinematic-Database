from time import sleep
from readFilms import read
from addFilms import insertFilms
from updateFilms import update
from deleteFilms import delete
import colorama
from colorama import Fore, Style, Back

# Initialize colorama
colorama.init()

def menuOptions():
    menuUI = f"""
{Fore.YELLOW}    SAFARIFLIX CINEMATIC DATABASE {Fore.BLUE}🚥 {Fore.GREEN}📶{Style.RESET_ALL}

{Fore.CYAN}    CHOOSE YOUR ADVENTURE:{Style.RESET_ALL}
        {Fore.MAGENTA}1. Explore films Catalogue in the Database...{Style.RESET_ALL}
        {Fore.MAGENTA}2. Introduce a New Masterpiece to your Database...{Style.RESET_ALL}
        {Fore.MAGENTA}3. Update an existing film...{Style.RESET_ALL}
        {Fore.MAGENTA}4. Permanently Delete an existing film...{Style.RESET_ALL}
        {Fore.MAGENTA}5. Exit the Viewing Expirience...{Style.RESET_ALL}
    """
    options = ["1", "2", "3", "4", "5"]
    choice = 0
    while choice not in options:
        print(menuUI)
        choice = input(f"{Fore.GREEN}Enter Select an Adventure from the menu: {Style.RESET_ALL}")
        if choice not in options:
            print(f"{Fore.RED}{choice} is not a valid option, try another adventure.{Style.RESET_ALL}")
            sleep(1)
    return choice

mainProgram = True
while mainProgram:
    userChoice = menuOptions()
    if userChoice == "1":
        read()
    elif userChoice == "2":
        insertFilms()
    elif userChoice == "3":
        update()
    elif userChoice == "4":
        delete()
    else:
        mainProgram = False

input(f"{Fore.YELLOW}Press Enter to Exit the Application.{Style.RESET_ALL}")
