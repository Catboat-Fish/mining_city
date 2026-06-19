import math
import sys
import disasters
from calc import *
from functions import *
from next_turn import next_turn
from stats import game_data


# to be reworked in graphics update alongside main_functions.py


#for thing, stuff in game_data["upgrade_cost"]["farm"].items():
#    if thing in game_data["resources"]:
#            print(f'{game_data["resources"][thing]}/{stuff}')

# test function
def test_function(quantity):
    if quantity == False:
        # go to menu command goes here
        pass
    else:
        print(f'Quantity / 2: {quantity / 2}')

# int input
def int_input(prompt):
    while True:
        value = input(prompt + "\n> ")

        if value.lower() in ("quit", "exit", "return", ""):
            return False
        try:
            int_value = int(value)
        except ValueError:
            print("Input a positive integer.")
            continue
        if int_value <= 0:
            print("Input a positive integer.")
            continue
        return int_value
