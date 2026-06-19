import math
from stats import game_data

# conversions to terms

city = game_data["city"]
resources = game_data["resources"]
stations = game_data["stations"]
cost = game_data["upgrade_cost"]
living = game_data["living"]

def total_workers(): # active workers
    return sum(s.get("workers", 0) + s.get("deployed", 0) for s in stations.values())

def total_adults():
    return living["residents"] + living["free_workers"] + total_workers()

def total_citizens(): # total people (for census purposes)
    return + living["children"] + living["teenagers"] + total_adults()

def total_people(): # total people + fetuses (for housing calculations)
    return living["fetuses"] + total_citizens()

def built_size(): # buildings
    return sum(s.get("size", 0) for s in stations.values())

def construction_size(): # buildings being built
    return sum(s.get("queue", 0) for s in stations.values())

def city_size(): # total city size
    return built_size() + construction_size()

def free_housing(): # total available house capacity (so there's never homelessness as that would break the game's balance)
    return stations["housing"]["size"] - total_people()

