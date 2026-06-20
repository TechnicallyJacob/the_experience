from funcs import intro

from player_object import player

while True:

    intro

    if player["health"] < 1:
        print(f"Good luck next time {player['name']}")
        break