import random 
from colorizer import *
from pyfiglet import figlet_format
from my_ascii_magic import intro, blackjack_win, bust



title = "Coding Nannah's Black Jack Game"

class Card:
    def __init__(self, suit, value):
        # Card as Parent Class?
        self.suit = suit
        self.value = value

    # __repr__() method to return string representation of a value
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

# test working: 
# card = Card("")

# dealer: own class? from deck? from hand?
# Deck of Cards API?
class Deck:
    def __init__(self):
        # every possible card of 52 for suit and for value - list comprehension!
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"]\
             for v in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]]

    def shuffle(self):
        # game usually has and uses 4 decks of cards; can be played with 1
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        # remove the top card from the deck, not to return
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    # Dealer False - not dealer hand
    def __init__(self, dealer=False):
        # dealing cards goes from Deck - full to Hand -empty
        self.dealer = dealer
        self.cards = []
        # starting value of counting cards
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    # card values change!
    # BEWARE! calculate_value is NOT a class. It is a function within class Hand

    def calculate_value(self):
        # starting value of counting cards
        self.value = value
        value = 0
        #loop through player's hand instance to add the value of player's cards
        for card in self.cards:
            # numbers are the value of the number
            if card.value.isnumeric():
                self.value += int(card,value)
            # Ace & Faces
            else:
                # Ace is special case:
                if card.value == "A":
                    # Dealer
                    dealer_hand_value = self.dealer_hand.get_value()
                    if dealer_hand_value < 17:
                        self.dealer.value += 11
                    else:
                        self.dealer.value += 1
                    # Player
                    one_or_11 = int(input("Would you like the value of this Ace to be 1 or 11? "))
                    while one_or_11 != 1 and one_or_11 != 11:
                        input("Please type either 1 or 11 as the value of this Ace. ")
                    if one_or_11 == 1:
                        self.value += 1
                    elif one_or_11 == 11:
                        self.value += 11
                else:
                    # value of other face cards
                    self.value += 10

    def get_value(self):
        self.calculate_value()
        self.player_hand.get_value()
        self.dealer_hand.get_value()
        return self.value

    # we want to SEE the hand(s)!
    def display(self):
        if self.dealer:
            #dealer's first face-down card
            print("hidden")
            #dealer's face-up card
            print(self.cards[1]) # [1] or (1)?
        else:
            for card in self.cards:
                print(card)
                print("Value:", self.get_value())

class Game:
    def __init__(self):
        pass

    def welcome():
        print(intro)

        name = input("Enter your name here: ").title()
        print(f"Welcome {name} to {title}!")

    # Boolean - playing or not?
    def play(self):
        playing = True

        while playing:
            # need shuffled deck - Deck of Cards API?
            self.deck = Deck()
            self.deck.shuffle()

            # need player and dealer hands
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            # using range() to deal two cards to each - from deck to hands
            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            # "See" the hands
            # Change this to visual cards with an API
            print("Your hand is: ")
            self.player_hand.display()
            print()
            print("Dealer's hand is: ")
            self.dealer_hand.display()

            # boolean while loop to run if game NOT over
            game_over = False
            while not game_over:

                # Blackjack = game over; check if no blackjack, so game still on
                player_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack: 
                    print(blackjack_win)
                    #Winner - must change game_over status
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack) # CHANGE THIS with magic and font in show results below
                    continue               
            
            # also in play section: hit or stand 
            choice = input("Do you [Hit / Stand]? ").lower()
            #if the input isn't understood
            while choice not in ["hit", "h", "stand", "s"]:
                choice = input("Please type either 'hit' or 'stand'. ")
            if choice in ["hit", "h"]:
                # choose to hit = add card to hand from deck
                self.player_hand.add_card(self.deck.deal())
                self.player_hand.display()
                # hit possibility is hand is over - check
                if self.player_is_over():
                    print(bust)
                    print("Your hand is over 21. You lose this round.")
                    game_over = True
            else:
                # this is the stand option
                # dealer must deal House faceup value >= 17
                while dealer_hand_value[1] < 17:
                    self.dealer_hand.add_card(self.deck.deal())

                # player's hand must be compared to the dealer's 
                player_hand_value = self.player_hand.get_value()
                dealer_hand_value = self.dealer_hand.get_value()

                #print hand statements:
                print("Final Results")
                print("Your hand:", player_hand_value)
                print("Dealer's hand:", dealer_hand_value)

                #compare hands & print win statements:
                if player_hand_value > dealer_hand_value:
                    print("You win this round!")
                elif player_hand_value == dealer_hand_value:
                    print("It's a tie. House wins this round!")
                else:
                    print("House wins this round!")
                game_over = True
        
        # outside play while loop: make it possible to play another round
        again = input("Would you like to play another round? [Y/N] ")
        while again.lower() not in ["y", "n"]:
            again = input("Please enter Y or N. ")
        if again.lower() == "n":
            # done = playing (no = false), game_over (yes = true)
            print(f"Thanks for playing {title}!")
            playing = False
        else:
            # play again = playing (yes = true), game_over (no = false)
            # game_over = False allows main loop to run again - back to top of self.deck = Deck()
            game_over = False


    def player_is_over(self):
        # boolean check if hand is over
        return self.player_hand.get_value() > 21

    def dealer_is_over(self):
        # boolean check if hand is over
        return self.dealer_hand.get_value() > 21
    

    # must tell computer how to check for blackjack:
    def check_for_blackjack(self):
        #which player has blackjack? Boolean for both:
        player = False
        dealer = False
        # check if either dealer or player have blackjack
        if self.player_hand.get_value() == 21:
            # Boolean value changes to true (yes, blackjack!) for whichever (or if each) has 21
            player = True
        # check if the other has blackjack
        if self.dealer_hand.get_value() == 21:
            # Boolean value changes to true (yes, blackjack!) for the other if it has 21
            dealer = True
            return player, dealer


    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        # if both have blackjack at the same time == draw
        if player_has_blackjack and dealer_has_blackjack:
            print("The player and the dealer have blackjack! It's a draw.")

        elif player_has_blackjack:
            print("You have blackjack! You win!")
        
        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")

        #game loop auto continues if neither has blackjack
        # in playing: player must choose to hit (add more cards) or stick with current cards


if __name__ == "__main__":
    game = Game()
    game.play()