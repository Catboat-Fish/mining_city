from main_functions import *


# to be reworked in graphics update alongside main_functions.py


# MENU FEATURES

# main game output WIP
def game_menu():
    pass

# save system WIP
def save_system():
    print("This is still a work in progress.")
    return

# load system WIP
def load_system():
    print("This is still a work in progress.")
    return

# main menu for starting the game
def main_menu():
    while True:
        print("Welcome to Mining City!\n\n1) New Game\n2) Load (WIP)\n3) Quit (WIP)")
        menu_choice = input("> ").strip()
        match menu_choice:
            case "1":
                game_menu()
            case "2":
                load_system()
            case "3":
                print("Exiting\n.\n.\n.")
                sys.exit()
            case _:
                print("Choose one of the options.")
        menu_choice = input("> ").strip()


# RUNS THE GAME


# runs the game if this code is in the "main.py" file
if __name__ == "__main__":

    wawa = int_input("How many?")
    test_function(wawa)

    #main_menu()

