# This program is a game where you try to get a magic book and bring it to a special library called The Archive

# Import necessary modules
from colorama import *
import story

# Define variables
game = 0

# Introduce title
print(Fore.BLUE + "Tales From an Evil Journal: A Quest for the Lost Book")

# Initial program requests
programStart = 1
while programStart == 1:
    race_type = input(Fore.GREEN + "What race would you like to play? (Dragonborn, Elf, or Wolf) ")
    race_type = race_type.lower()
    player_name = input("Please, tell us your name: ")
    if race_type == "dragonborn" or race_type == "elf" or race_type == "wolf":
        game = 1
    else:
        print(Fore.RED + "Invalid race type.")

# Starting the game
    while game == 1:
        story.sectionOne()
        print("The bartender approaches you while drying a few glasses. 'Ya seem quite interested in that there plaque. You another")
        print("one of them brash explorers?'")
        isExperienced = input("(yes or no) ")
