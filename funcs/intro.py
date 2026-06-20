import time
from objs.player_object import player
from funcs import town, forest

player_name = input("Hello traveler! What is your name so we can get this adventure started!? ")
player['name'] = player_name
time.sleep(2)

message0 = f"Ahh {player['name']}, I once knew a {player['name']}, unfortunately they took an arrow to the knee and died from syphilis."
print(message0)
time.sleep(2)

message1 = f"Hahaha, nevermind that {player['name']}, what is your main archetype? 'Warrior', 'Mage', or 'Ranger'? " 
player_archetype = input(message1).strip().lower()
time.sleep(2)

if player_archetype == "warrior":

    print("Ahh a warrior, I see you like to get up close and personal with your enemies, good choice!")
    time.sleep(2)

    print("Here's a sword and 100 gold to get you started, it's not much but it'll do for now.")
    time.sleep(2)

    player["weapon"] = "sword"
    player["physical"] = 2
    player["strength"] += 2
    player["constitution"] += 2
    player["physical"] += 2

elif player_archetype == "mage":

    print("Ahh a mage, I see you like to manipulate the elements, good choice!")
    time.sleep(2)
    print("Here's a wand and 100 gold to get you started, it's not much but it'll do for now.")
    time.sleep(2)

    player["weapon"] = "wand"
    player["magicka"] = 2
    player["intellect"] += 2
    player["magicka"] += 2
    player["mana"] += 2

elif player_archetype == "ranger":

    print("Ahh a ranger, I see you like to keep your distance and strike from afar, good choice!")
    time.sleep(2)

    print("Here's a bow and 100 gold to get you started, it's not much but it'll do for now.")
    time.sleep(2)

    player["weapon"] = "bow"
    player["ranged"] = 2
    player["ranged"] += 2
    player["agility"] += 2
    player["stealth"] += 2
    player["dodge"] += 2

else:
    print("Invalid input, please try again.")
    time.sleep(2)
player["gold"] += 100

print("You can head into town to buy items and gear from the shopkeeper.")
time.sleep(2)

print(f"Or you can head out into the wilderness and start fighting some enemies to level up and get some loot!")
time.sleep(2)

print("You can check your stats and inventory at any time by typing 'stats' or 'inventory' in the command prompt, and you can check your current gold by typing 'gold'.")
time.sleep(2)

print(f"Let's get this adventure started {player['name']} the {player_archetype.title()}!")
time.sleep(2)
print()