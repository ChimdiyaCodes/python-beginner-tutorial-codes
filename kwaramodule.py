# creating a module

from random import choice

capital = "Ilorin"
geography = "north central"


def randomfunfact():
    funfacts = [
        "Ilorin, the capital of Kwara state is known for its rich history.",
        "Worthy of note is its diverse culture and significance as a center of Islamic learning.",
        "It has a strong Yoruba influence and is also deeply connected to the Hausa and Fulani cultures."
    ]

    print(choice(funfacts))  # Directly selects a random fact


if __name__ == "__main__":
    randomfunfact()
