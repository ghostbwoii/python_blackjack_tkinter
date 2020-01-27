"""
creates a deck object
"""

import random
from colorama import Fore, Back, Style
from Playing_Card import Card


class Deck(Card):
    """
    generates a deck of cards. shuffles deck of cards
    """

    deck = []

    def __init__(self):
        pass

    def generate_deck(self):
        """
        generates a deck of 52 cards
        """
        index = 0
        for i in self.card_suit:
            counter = 0
            for j in self.card_type:
                one = Card(i, j, self.card_value[counter], self.card_value_two[counter],
                           self.card_images[index], Fore.BLUE + Back.WHITE + Style.BRIGHT +
                           " x x x \n  x x  \n x x x \n  x x  \n x x x " + Style.RESET_ALL)
                self.deck.append(one)
                counter += 1
                index += 1

        return self.deck

    def shuffle_deck(self, deck):
        """
        shuffles the deck 50 times
        """
        temp = None
        for i in range(0, 50):
            counter = 0
            random_num = random.randint(0, len(deck) - 1)
            while counter < len(deck):

                temp = deck[counter]
                deck[counter] = deck[random_num]
                deck[random_num] = temp
                counter += 1
        return deck

    def print_deck(self, deck):
        """
        prints the deck if needed
        """
        for i in deck:
            print(i.get_suit() + " " + i.get_card_type() + " "
                  + str(i.get_card_value()) + " " + str(i.get_card_value_two()))

    def get_deck(self):
        """
        returns deck once filled if needed
        """
        return self.deck
