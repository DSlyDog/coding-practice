# This program is a game where you try to get a magic book and bring it to a special library called The Archive

# Import necessary modules
from colorama import *
import story

# Introduce title
print(Fore.BLUE + "Tales From an Evil Journal: A Quest for the Lost Book")

# Initial program requests
programStart = 1
while programStart == 1:
    race_type = input(Fore.GREEN + "What race would you like to play? (Dragonborn, Elf, or Wolf) ")
    player_name = input("Please, tell us your name: ")
    game = 1

# Starting the game
    while game == 1:
        story.sectionOne()
