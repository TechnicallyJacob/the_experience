import time

from funcs import intro, town, forest

from objs.player_object import player

user_input = ""

while True:

    intro

    user_input = input("What would you like to do? \nChoices = 'gold', 'inventory', 'stats', 'town', 'forest', 'end' \n").strip().lower()

    while True:
        if user_input.strip().lower() == "gold":
            print(player["gold"])
            time.sleep(0.5)
            break
        elif user_input.strip().lower() == "inventory":
            print(player["weapon"])
            time.sleep(0.5)
            print(player["armor"])
            time.sleep(0.5)
            print(f"Health Potions: {player['health_potions']}")
            time.sleep(0.5)
            print(f"Mana Potions: {player['mana_potions']}")
            time.sleep(0.5)
            print(f"Stamina Potions: {player['stamina_potions']}")
            time.sleep(0.5)
            break
        elif user_input.strip().lower() == "stats":
            print(f"Health: {player['health']}")
            time.sleep(0.5)
            print(f"Stamina: {player['stamina']}")
            time.sleep(0.5)
            print(f"Mana: {player['mana']}")
            time.sleep(0.5)
            print(f"Strength: {player['strength']}")
            time.sleep(0.5)
            print(f"Intellect: {player['intellect']}")
            time.sleep(0.5)
            print(f"Agility: {player['agility']}")
            time.sleep(0.5)
            print(f"Constitution: {player['constitution']}")
            time.sleep(0.5)
            print(f"Physical: {player['physical']}")
            time.sleep(0.5)
            print(f"Magicka: {player['magicka']}")
            time.sleep(0.5)
            print(f"Ranged: {player['ranged']}")
            time.sleep(0.5)
            print(f"Dodge: {player['dodge']}")
            time.sleep(0.5)
            print(f"Stealth: {player['stealth']}")
            time.sleep(0.5)
            break
        elif user_input.strip().lower() == "town":
            town()
            break
        elif user_input.strip().lower() == "forest":
            forest()
            break
        else:
            print("Invalid input, please try again.")
            time.sleep(3)
            break
    if user_input.strip().lower() == "end":
        print(f"Goodbye {player['name']}!")
        player["health"] = 0
        break

    if player["health"] == 0:
        print(f"Good luck next time {player['name']}")
        break