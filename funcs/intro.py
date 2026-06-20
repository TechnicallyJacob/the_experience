from player_object import player
from funcs import town, forest

player_name = input("Hello traveler! What is your name so we can get this adventure started!? ")
player['name'] = player_name
message0 = f"Ahh {player['name']}, I once knew a {player['name']}, unfortunately they took an arrow to the knee and died from syphilis."
print(message0)
message1 = f"Hahaha, nevermind that {player['name']}, what is your main archetype? 'warrior', 'mage', or 'ranger'? " 
player_archetype = input(message1)
if player_archetype == "warrior":
    print("Ahh a warrior, I see you like to get up close and personal with your enemies, good choice!")
    print("Here's a sword to get you started, it's not the best but it'll do for now.")
    player["weapon"] = "sword"
    player["physical"] = 2
    player["strength"] += 2
    player["constitution"] += 2
    player["physical"] += 2
elif player_archetype == "mage":
    print("Ahh a mage, I see you like to manipulate the elements, good choice!")
    print("Here's a wand to get you started, it's not the best but it'll do for now.")
    player["weapon"] = "wand"
    player["magicka"] = 2
    player["intellect"] += 2
    player["magicka"] += 2
    player["mana"] += 2
elif player_archetype == "ranger":
    print("Ahh a ranger, I see you like to keep your distance and strike from afar, good choice!")
    print("Here's a bow to get you started, it's not the best but it'll do for now.")
    player["weapon"] = "bow"
    player["ranged"] = 2
    player["ranged"] += 2
    player["agility"] += 2
    player["stealth"] += 2
    player["dodge"] += 2
else:
    print("Invalid input, please try again.")
print(f"Great, now that we have your name and archetype, let's get this adventure started {player['name']} the {player_archetype}!")
print("Here's some gold to get you started on your adventure, you can use it to buy items and gear from the shopkeeper in town.")
player["gold"] += 100
print(f"You can head into town and talk to the shopkeeper to buy some armor and potions, or you can head out into the wilderness and start fighting some enemies to level up and get some loot! The choice is yours, good luck on your adventure {player['name']}!")
print("You can check your stats and inventory at any time by typing 'stats' or 'inventory' in the command prompt, and you can check your current gold by typing 'gold'.")
print("Where would you like to go? 'town' or to the 'forest'?")
if input() == "town":
    town()
elif input() == "forest":
    forest()
else:
    print("Invalid input, please try again.")