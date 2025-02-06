def hello(name, lang):
    greetings = {
        "English": "Good morning",
        "Yoruba": "Ekaaro",
        "Igbo": "Ututu oma",
        "Hausa": "Ina kwana"
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)


if __name__ == '__main__':

    import argparse  # import argparse module used to handle command line arguments

    # Create a parser
    # a parser helps the computer read the command line argument
    # the argparse module provides an ArgumentParser object, which:
    # ✅ Understands what arguments the user should provide.
    # ✅ Processes those arguments and gives them to the program.
    # ✅ Displays help messages when needed.
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting.")

    # Add an argument
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Yoruba", "Igbo", "Hausa"],
        help="The language of the greeting."
    )

    # Parse the arguments
    args = parser.parse_args()

    hello(args.name, args.lang)

    # the command for my terminal: py hello_person.py -n Chimdiya -l Igbo
    # py hello_person.py -n Chimdiya -l Yoruba
    # py hello_person.py -n Chimdiya -l Hausa
    # py hello_person.py -n Chimdiya -l English
