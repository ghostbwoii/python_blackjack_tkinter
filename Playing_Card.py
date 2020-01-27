"""
creates card object
"""

from colorama import Back, Fore, Style

class Card:
    """
    creates a card object that is used to create a deck object
    """
    card_suit = ["SPADES", "CLUBS", "DIAMONDS", "HEARTS"]
    suit = None
    card_type = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
                 "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]
    c_type = None
    card_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    value = None
    card_value_two = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    value_two = None
    card_image = None
    blank_image = None
    card_images = [
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " A   A \n       \n   \u2660   \n       \n A   A " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 2   2 \n       \n   \u2660   \n       \n 2   2 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 3   3 \n       \n   \u2660   \n       \n 3   3 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 4   4 \n       \n   \u2660   \n       \n 4   4 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 5   5 \n       \n   \u2660   \n       \n 5   5 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 6   6 \n       \n   \u2660   \n       \n 6   6 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 7   7 \n       \n   \u2660   \n       \n 7   7 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 8   8 \n       \n   \u2660   \n       \n 8   8 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 9   9 \n       \n   \u2660   \n       \n 9   9 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 10 10 \n       \n   \u2660   \n       \n 10 10 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " J   J \n       \n   \u2660   \n       \n J   J " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " Q   Q \n       \n   \u2660   \n       \n Q   Q " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " K   K \n       \n   \u2660   \n       \n K   K " + Style.RESET_ALL,

        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " A   A \n       \n   \u2663   \n       \n A   A " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 2   2 \n       \n   \u2663   \n       \n 2   2 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 3   3 \n       \n   \u2663   \n       \n 3   3 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 4   4 \n       \n   \u2663   \n       \n 4   4 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 5   5 \n       \n   \u2663   \n       \n 5   5 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 6   6 \n       \n   \u2663   \n       \n 6   6 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 7   7 \n       \n   \u2663   \n       \n 7   7 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 8   8 \n       \n   \u2663   \n       \n 8   8 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 9   9 \n       \n   \u2663   \n       \n 9   9 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " 10 10 \n       \n   \u2663   \n       \n 10 10 " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " J   J \n       \n   \u2663   \n       \n J   J " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " Q   Q \n       \n   \u2663   \n       \n Q   Q " + Style.RESET_ALL,
        Fore.BLACK + Back.WHITE + Style.BRIGHT +
        " K   K \n       \n   \u2663   \n       \n K   K " + Style.RESET_ALL,

        Fore.RED + Back.WHITE + Style.BRIGHT +
        " A   A \n       \n   \u2666   \n       \n A   A " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 2   2 \n       \n   \u2666   \n       \n 2   2 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 3   3 \n       \n   \u2666   \n       \n 3   3 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 4   4 \n       \n   \u2666   \n       \n 4   4 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 5   5 \n       \n   \u2666   \n       \n 5   5 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 6   6 \n       \n   \u2666   \n       \n 6   6 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 7   7 \n       \n   \u2666   \n       \n 7   7 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 8   8 \n       \n   \u2666   \n       \n 8   8 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 9   9 \n       \n   \u2666   \n       \n 9   9 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 10 10 \n       \n   \u2666   \n       \n 10 10 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " J   J \n       \n   \u2666   \n       \n J   J " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " Q   Q \n       \n   \u2666   \n       \n Q   Q " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " K   K \n       \n   \u2666   \n       \n K   K " + Style.RESET_ALL,

        Fore.RED + Back.WHITE + Style.BRIGHT +
        " A   A \n       \n   \u2665   \n       \n A   A " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 2   2 \n       \n   \u2665   \n       \n 2   2 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 3   3 \n       \n   \u2665   \n       \n 3   3 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 4   4 \n       \n   \u2665   \n       \n 4   4 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 5   5 \n       \n   \u2665   \n       \n 5   5 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 6   6 \n       \n   \u2665   \n       \n 6   6 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 7   7 \n       \n   \u2665   \n       \n 7   7 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 8   8 \n       \n   \u2665   \n       \n 8   8 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 9   9 \n       \n   \u2665   \n       \n 9   9 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " 10 10 \n       \n   \u2665   \n       \n 10 10 " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " J   J \n       \n   \u2665   \n       \n J   J " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " Q   Q \n       \n   \u2665   \n       \n Q   Q " + Style.RESET_ALL,
        Fore.RED + Back.WHITE + Style.BRIGHT +
        " K   K \n       \n   \u2665   \n       \n K   K " + Style.RESET_ALL]



    def __init__(self, suit, c_type, value, value_two, card_image, blank_image):
        self.suit = suit
        self.c_type = c_type
        self.value = value
        self.value_two = value_two
        self.card_image = card_image
        self.blank_image = blank_image

    def get_suit(self):
        """
        returns suit for card obj
        """
        return self.suit

    def get_card_type(self):
        """
        returns type for card obj
        """
        return self.c_type

    def get_card_value(self):
        """
        returns value for card
        """
        return self.value

    def get_card_value_two(self):
        """
        returns alternate set of values for card to reflect varying ace value
        """
        return self.value_two
    def get_card_image(self):
        """
        gets ascii image of card
        """
        return self.card_image

    def get_blank(self):
        """
        gets back side of card
        """
        return self.blank_image
