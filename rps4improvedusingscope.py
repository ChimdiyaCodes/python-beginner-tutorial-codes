# improving rps using recursive function

import sys
import random
from enum import Enum

game_count = 0


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computer = random.randint(1, 3)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '').title() + ".\n")

    def decide_winner(player, computer):

        if (player == 1 and computer == 3) or \
            (player == 2 and computer == 1) or \
                (player == 3 and computer == 2):

            return "🎉 YOU WIN!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 PYTHON WINS"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉 🎉 🎉 🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
