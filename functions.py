import math
from calc import *
from stats import game_data


# definitions

def make_worker(quantity):
    if not isinstance(quantity, int) or quantity <= 0:
        return 'Input a positive integer.'
    elif quantity > resources["tools"]:
            return f'Not enough tools ({resources["tools"]}/{quantity}). Assign workers to the factory.'
    elif quantity > living["residents"]:
        return f'Not enough residents ({living["residents"]}/{quantity}). More children need to be born and grow up.'
    else:
        living["residents"] -= quantity
        living["free_workers"] += quantity
        return f'{city["name"]} has successfully recruited {quantity} free workers. Remember to assign them to a station.'   

def assign_worker(station, quantity):
    if not isinstance(quantity, int) or quantity <= 0:
        return 'Input a positive integer.'
    elif quantity > living["free_workers"]:
        return f'Not enough free workers ({living["free_workers"]}/{quantity}). Equip more residents with tools.'
    else:
        living["free_workers"] -= quantity
        stations[station]["workers"] += quantity
        return f'{city["name"]} has successfully assigned {quantity} workers to the {station}. They will produce resources at the end of every turn.'

def make_babies(quantity):
    housing = free_housing() # reduces calls
    fertile_people = (living["residents"] + living["free_workers"] + total_workers())
    if not isinstance(quantity, int) or quantity <= 0:
        return 'Input a positive integer.'
    elif quantity > housing:
        return f'Not enough free housing ({housing}/{quantity}). Build more housing at the construction site.'
    elif (quantity + living["fetuses"]) > resources["food"]:
        return f'Not enough food ({resources["food"]}/{quantity + living["fetuses"]}). Assign workers to the farm.'
    elif  quantity * 2 > fertile_people:
        return f'Not enough adults ({fertile_people}/{quantity * 2}). You need at least two adults (worker, free worker, or resident) for every baby.'
    else:
        living["fetuses"] += quantity
        return f'{city["name"]} has successfully created {quantity} babies. Wait one turn for them to be born and three turns for them to become adults.'     

def expand_housing(quantity): #WIP
    if not isinstance(quantity, int) or quantity <= 0:
        return 'Input a positive integer.'
    if (quantity * cost["house"]["wood"]) > resources["wood"]: # resource calculator, replace once better is built in expand_station
        return f'Not enough resources ({resources["wood"]}/{quantity * cost["house"]["wood"]}). Assign workers to the lumber mill.'
    elif math.ceil(quantity / 10) > stations["construction"]["workers"]: # 10 houses per worker
        return f'Not enough workers(stations["construction"]["workers"]/{math.ceil(quantity / 10)}). Assign workers to the construction site.'
    else:
        return f'{city["name"]} has successfully started construction on {quantity} houses. Wait one turn for them to be built.'

def expand_station(station, quantity): # WIP, make seperate function for housing later
    # costs[] = cost[station]
    if False:
        pass
    #elif not isinstance(quantity, int) or quantity <= 0:
    #    return 'Input a positive integer.'
    elif (quantity) > stations["construction"]["workers"]:
        return f'Not enough construction workers ({stations["construction"]["workers"]}/{quantity}). Assign more to the construction site.'
    else:
        return f'{city["name"]} has successfully started construction on {quantity} houses. Wait one turn for them to be built.'


# templates
    # on success
        # return '{city["name"]} has successfully... [created, recruited, assigned]
    # on failure
        # return 'Not enough {thing} ({amount}/{needed}).'
        # either or
            # 'Build more {thing} at the construction site.'
            # 'Assign workers to the {place}.'
    # pos int checker
        # if not isinstance(quantity, or) or quantity <= 0:
            # return 'Input a positive integer.'
    # error guide
        # if not pos_int... elif few stations... elif few resources... elif few workers

