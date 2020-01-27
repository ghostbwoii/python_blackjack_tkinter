"""
creates game logic, theres a rare situation where is dealer busts
"""
import msvcrt
import re
import sys
import os
import time
from colorama import Fore, Back, Style
from Deck_Of_Cards import Deck
from Login_Interface import Login


class Play(Deck):
    """
    class holds game logic
    """

    os.system("mode con: cols=200 lines=200")
    os.system("color 0")
    player_hand = []
    dealer_hand = []
    deck_of_cards = []
    counter = 0
    user_input = None
    win_flag = False

    def __init__(self):
        """
        default constructor
        """

    def play_game(self):
        """
        logic for the blackjack game
        """

        print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT
              + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to Black Jack !!!"
              + Style.RESET_ALL)
        time.sleep(3)
        os.system("cls")

        self.deck_of_cards = self.shuffle_deck(self.generate_deck())
        while True:
            os.system("mode con: cols=200 lines=200")
            os.system("color 0")
            self.win_flag = False
            self.deal_cards()
            if self.counter == 4:
                self.display_dealer_hand(self.player_hand)

                self.display_dealer_hand(self.dealer_hand)

                if self.win_conditions(self.win_flag):
                    continue
                while True:

                    print(Fore.WHITE + Back.YELLOW +  Style.BRIGHT + "\n\n1 - Hit" +
                          (" " * 12) + "2 - Stay" + (" " * 12) + "3 - Quit\n\n" + Style.RESET_ALL)
                    try:
                        self.user_input = str(int(msvcrt.getch()))
                    except ValueError:
                        pass

                    if self.user_input == '1' and re.findall("^[0-9]?$", self.user_input):
                        self.user_hit()

                        if self.win_conditions(self.win_flag):
                            os.system('cls')
                            os.system("mode con: cols=200 lines=200")
                            os.system("color 0")
                            break

                    if self.user_input == '2' and re.findall("^[0-9]?$", self.user_input):

                        self.user_stay()
                        self.win_conditions(self.win_flag)
                        os.system('cls')
                        os.system("mode con: cols=200 lines=200")
                        os.system("color 0")
                        break

                    if self.user_input == '3' and re.findall("^[0-9]?$", self.user_input):
                        print("\n\n"+ Back.MAGENTA + Fore.WHITE + Style.BRIGHT)
                        print(f"{'Thanks for playing!':^129}")
                        sys.exit(1)
                    else:
                        pass

    def deal_cards(self):
        """
        deals the first cards to both player and dealer
        """
        if self.counter < 2:
            self.player_hand.append(self.deck_of_cards[0])
            self.deck_of_cards.remove(self.deck_of_cards[0])
            self.counter += 1
        if self.counter >= 2 and self.counter < 4:
            self.dealer_hand.append(self.deck_of_cards[0])
            self.deck_of_cards.remove(self.deck_of_cards[0])
            self.counter += 1

    def win_conditions(self, win_flag):
        """
        determines win or loss
        """

        player_sum = self.find_sum(self.player_hand)
        dealer_sum = self.find_sum(self.dealer_hand)
        loop_control = False
        if player_sum == 21:
            os.system("cls")
            os.system("color 0")
            print(Back.BLACK + Fore.GREEN
                  + Style.BRIGHT + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou win!!!"
                  + Style.RESET_ALL + " Player " + str(player_sum) + "  Dealer " + str(dealer_sum))
            self.pause_screen()
            self.counter = 0
            loop_control = True
            self.empty_hand()
            #self.deck_of_cards = self.shuffle_deck(self.generate_deck())


        if dealer_sum > 21:
            os.system("cls")
            os.system("color 0")
            print(Back.BLACK + Fore.GREEN
                  + Style.BRIGHT + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou win!!!"
                  + Style.RESET_ALL + " Player " + str(player_sum) + "  Dealer " + str(dealer_sum))
            self.pause_screen()
            self.counter = 0
            loop_control = True
            self.empty_hand()
            #self.deck_of_cards = self.shuffle_deck(self.generate_deck())


        if player_sum > 21:
            os.system("cls")
            os.system("color 0")
            print(Back.BLACK + Fore.RED
                  + Style.BRIGHT + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou lose!!!"
                  + Style.RESET_ALL + " Player " + str(player_sum) + "  Dealer " + str(dealer_sum))

            self.pause_screen()
            self.counter = 0
            loop_control = True
            self.empty_hand()
            #self.deck_of_cards = self.shuffle_deck(self.generate_deck())


        if player_sum <= 21 and win_flag is True:
            if player_sum > dealer_sum:
                os.system("cls")
                os.system("color 0")
                print(Back.BLACK + Fore.GREEN
                      + Style.BRIGHT + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou win!!!"
                      + Style.RESET_ALL + " Player "
                      + str(player_sum) + "  Dealer " + str(dealer_sum))
                self.pause_screen()
                self.counter = 0
                loop_control = True
                self.empty_hand()
                #self.deck_of_cards = self.shuffle_deck(self.generate_deck())


            if player_sum <= dealer_sum and dealer_sum <= 21:
                os.system("cls")
                os.system("color 0")
                print(Back.BLACK + Fore.RED
                      + Style.BRIGHT + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou lose!!!"
                      + Style.RESET_ALL + " Player "
                      + str(player_sum) + "  Dealer " + str(dealer_sum))
                self.pause_screen()
                self.counter = 0
                loop_control = True
                self.empty_hand()
                #self.deck_of_cards = self.shuffle_deck(self.generate_deck())


            if player_sum <= dealer_sum and dealer_sum >= 21:
                os.system("cls")
                os.system("color 0")
                print(Back.BLACK + Fore.GREEN
                      + Style.BRIGHT + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou win!!!"
                      + Style.RESET_ALL + " Player "
                      + str(player_sum) + "  Dealer " + str(dealer_sum))
                self.pause_screen()
                self.counter = 0
                loop_control = True
                self.empty_hand()
                #self.deck_of_cards = self.shuffle_deck(self.generate_deck())

        return loop_control


    def user_hit(self):
        """
        handles user input to hit
        """
        self.player_hand.append(self.deck_of_cards[0])
        self.deck_of_cards.remove(self.deck_of_cards[0])
        os.system('cls')
        os.system("mode con: cols=200 lines=200")
        os.system("color 0")
        self.display_dealer_hand(self.player_hand)
        self.display_dealer_hand(self.dealer_hand)
        time.sleep(2)


    def pause_screen(self):
        """
        ad hoc method to pause screen after win conditions
        """
        time.sleep(3)
        os.system("cls")

    def user_stay(self):
        """
        handles user input to stay
        """
        os.system("cls")
        os.system("color 0")
        self.display_hand(self.player_hand)
        self.display_hand(self.dealer_hand)
        time.sleep(2)

        if self.find_sum(self.dealer_hand) < 16:
            self.dealer_hand.append(self.deck_of_cards[0])
            self.deck_of_cards.remove(self.deck_of_cards[0])
            os.system("cls")
            os.system("color 0")
            self.display_hand(self.player_hand)
            self.display_hand(self.dealer_hand)
            time.sleep(3)
            self.win_conditions(self.win_flag)
            self.counter = 0
            self.win_flag = True

        self.counter = 0
        self.win_flag = True


    def empty_hand(self):
        """
        empties both hands
        """

        self.player_hand = []
        self.dealer_hand = []


    def display_dealer_hand(self, hand):
        """
        displays dealer hand when one card is facedown
        """
        if hand == self.player_hand:
            print(Fore.WHITE + Back.GREEN + Style.BRIGHT + "Player:\n" + Style.RESET_ALL)
            for i in hand:
                print(i.get_card_image() + "\n")
        else:
            print(Fore.WHITE + Back.RED + Style.BRIGHT + "Dealer:\n\n" + Style.RESET_ALL
                  + hand[0].get_card_image() + "\n\n" + hand[0].get_blank())



    def display_hand(self, hand):
        """
        outputs hand
        """
        if hand == self.player_hand:
            print(Fore.WHITE + Back.BLUE + Style.BRIGHT + "Player:\n" + Style.RESET_ALL)
            for i in hand:
                print(i.get_card_image() + "\n\n")
        else:
            print(Fore.WHITE + Back.RED + Style.BRIGHT + "Dealer:\n" + Style.RESET_ALL)
            for i in hand:
                print(i.get_card_image() + "\n\n")


    def find_sum(self, hand):
        """
        finds sum of the cards in a hand
        """
        card_sum = 0
        card_sum_two = 0
        for i in hand:
            if i is not None:
                card_sum += i.get_card_value()
                card_sum_two += i.get_card_value_two()
        if card_sum > 21:
            if card_sum_two <= 21:
                return card_sum_two

        return card_sum





def main():
    """
    used to launch app
    """
    try:
        one = Login()
        one.set_grid(one.create_nodes(one.create_scene())).mainloop()
        if one.get_permission():
            two = Play()
            two.play_game()
    except ImportError:
        print("Module not found")
        sys.exit(1)
    except EOFError:
        print("No value was entered")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Forced App. Shutdown")
        sys.exit(1)
    except OSError:
        print("Operating system compatibility.")
        sys.exit(1)
    except IndexError:
        print("Exceeded list index")
        sys.exit(1)
    except UnicodeError:
        print("Card emblem not 'rendered' correctly")
        sys.exit(1)
    except RuntimeError:
        print("Error encountered. App. shutdown")
        sys.exit(1)

if __name__ == "__main__":
    main()
