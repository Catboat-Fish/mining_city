import math
import random
from calc import *
from functions import *
from stats import game_data


random.seed()

# conversions to terms

social = game_data["social_disasters"]
natural = game_data["natural_disasters"]
shortage = game_data["social_disasters"]["shortage"]

# commands and things to run in next_turn.py

def disaster_check(): # WIP
    total_pop = total_citizens()
    # shortage
    if total_pop + stations["factory"]["workers"] < resources["coal"]:
        amount = math.ceil(total_pop + stations["factory"]["workers"] - resources["coal"]) # amount of inefficient workers
        factory_reduction(amount)
    if total_pop < resources["food"] or total_pop < resources["coal"]:
        shortage["status"] = True
        shortage()
    else:
        shortage["status"] = False

def pop_decrease(amount): # WIP
    pass

def unrest_check():
    unrest = social["unrest"]
    if unrest == 0: # 0
        social["minor_chance"] = 1
        social["moderate_chance"] = 0
        social["major_chance"] = 0
    elif unrest < 10: # 1-9
        social["minor_chance"] = 5
        social["moderate_chance"] = 0
        social["major_chance"] = 0
    elif unrest < 20: # 10-19
        social["minor_chance"] = 15
        social["moderate_chance"] = 10
        social["major_chance"] = 0
    elif unrest >= 20: # 20+
        social["minor_chance"] = 1
        social["moderate_chance"] = 0
        social["major_chance"] = 0


def clear_disasters(): # WIP, used at end of turn after all disasters play out
    # social disasters

    shortage["factory_reduction"] = 0
    # natural disasters
    pass

# social disasters

def random_social_disaster(): # WIP
    pass

def shortage(): # WIP
    total_pop = total_citizens()
    shortage_amount = 0
    if total_citizens() < resources["food"]:
        shortage_amount += max(total_pop - resources["food"], math.ceil()) # 

def factory_reduction(amount): # WIP
    shortage["factory_reduction"] = amount
    
# natural disasters

def random_natural_disaster(): # WIP
    pass
