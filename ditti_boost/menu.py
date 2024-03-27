from colorama import Fore, Style, init
init()

def display_menu():
    print(Fore.CYAN + "1. Follow")
    print("2. Unfollow")
    return input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

def display_follow_scripts():
    print(Fore.CYAN + "1. Copy a user's following")
    print("2. Follow (x) new users")
    print("3. Follow collection owners")
    return input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

def display_unfollow_scripts():
    print(Fore.CYAN + "1. Unfollow all users")
    print("2. Unfollow non-follow back users")
    print("3. Unfollow collection owners")
    print("4. Unfollow users with no casts")
    print("5. Unfollow users not casting within (x) days")
    return input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)
