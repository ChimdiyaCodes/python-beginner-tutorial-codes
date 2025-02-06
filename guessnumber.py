# improving rps using f string function

import sys
import random


def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guessnumber():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, guess what number I'm thinking of...\n1 ,\n2 , or \n3 :\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guessnumber()

        computer = random.randint(1, 3)

        print(
            f"\n{name}, you chose {playerchoice}.")
        print(
            f"I was thinking about the number {str(computer)}.\n")

        player = int(playerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"Congratulations 🎉 {name}, You guessed right!"
            else:
                return f"\nSorry, {name}..😟 better luck next time!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")

        print(f"\nYour percentage win: {player_wins/game_count:.0%}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guessnumber()
        else:
            print("\n🎉 🎉 🎉 🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return

    return play_guessnumber


if __name__ == "__main__":

    import argparse  # import argparse module used to handle command line arguments

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience.")

    # Add an argument
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    # Parse the arguments
    args = parser.parse_args()

    guess_the_number = guess_number(args.name)
    guess_the_number()

    # command prompt for terminal: py guessnumber.py -n Chimdiya
