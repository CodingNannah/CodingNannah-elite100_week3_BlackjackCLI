import random
import time
from colorizer import *
from pyfiglet import figlet_format
from my_ascii_magic import intro, blackjack_win, bust


title = "Coding Nannah's Black Jack Game"
suit = ["♠", "♣", "♡", "♢"]
label = [' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', ' J', ' Q', ' K', ' A']
full_deck = [f"{j} of {i}" for j in label for i in suit]*4
deck = full_deck[:]
error = print_red("Oops, Let's try that again.")


class Card:
    def __init__(self, suit, label):
        self.suit = suit
        self.label = label

    def value (self, hand):
        value = 0
        for i in hand:
            if i[0][1] in ('J', 'Q', 'K', '0'):
                value += 10
            elif i[0][1] == 'A':
                value += 11
            else:
                value += int(i[0][1])
        if value <= 21:
            return value
        elif value > 21:
            for i in hand:
                if i[0][1] != 'A':
                    return value
                if i[0][1] == 'A':
                    value -= 10
            else:
                return value

    """ Not here - belongs with HAND
       # __repr__() method to return string representation of a value
    def __repr__(self):
        return "{} of {}".format(self.label, self.suit)"""

    """Trying to get card appearance to code only ONCE"""
    # def appearance(self):
    #     for i in range(1):                       # hand.hand[i][0][0:2]
    #             print(f' ______\t'*len(hand.hand))
    #             print(f'|{a}    |'+f'|{b}    |')
    #             print(f'|      |'*len(hand.hand))
    #             print(f'|      |'*len(hand.hand))
    #             print(f'|____{a}|'+f'|____{b}|\n')

class Dealer(Card):
    
    def __init__(self):
        self.name = name
        name ='Monty'
        self.hand = []      

    def hidden_hand(self):
        print(f"Dealer's hand:")
        while self.hand[1][0][0] == '1':                     
            y = self.hand[1][0][0:2]

        for i in range(1):
            print(f' ______\t'+f' ______\t')
            print(f'|# # # |'+f'|{y}    |')
            print(f'| # # #|'+f'|      |')
            print(f'|# # # |'+f'|      |')
            print(f'|_#_#_#|'+f'|____{y}|\n')
        
    def reveal_hand(self):
        print(f"{self.name}'s hand:")         
        a = self.hand[0][0][0:2]
        b = self.hand[1][0][0:2]
 
        if len(self.hand) == 2:                      # [[' 4 of hearts'], [' 7 of hearts']]
            for i in range(1):                       # self.hand[i][0][0:2]
                print(f' ______\t'*len(self.hand))
                print(f'|{a}    |'+f'|{b}    |')
                print(f'|      |'*len(self.hand))
                print(f'|      |'*len(self.hand))
                print(f'|____{a}|'+f'|____{b}|\n')
        elif len(self.hand) == 3:
            c = self.hand[2][0][0:2]
            for i in range(1):
                print(f' ______\t'*len(self.hand))
                print(f'|{a}    |'+f'|{b}    |'+f'|{c}    |')
                print(f'|      |'*len(self.hand))
                print(f'|      |'*len(self.hand))
                print(f'|____{a}|'+f'|____{b}|'+f'|____{c}|\n')
        elif len(self.hand) == 4:
            c = self.hand[2][0][0:2]
            d = self.hand[3][0][0:2]
            for i in range(1):
                print(f' ______\t'*len(self.hand))
                print(f'|{a}    |'+f'|{b}    |'+f'|{c}    |'+f'|{d}    |')
                print(f'|      |'*len(self.hand))
                print(f'|      |'*len(self.hand))
                print(f'|____{a}|'+f'|____{b}|'+f'|____{c}|'+f'|____{d}|\n')
        elif len(self.hand) == 5:
            c = self.hand[2][0][0:2]
            d = self.hand[3][0][0:2]
            e = self.hand[4][0][0:2]
            for i in range(1):
                print(f' ______\t'*len(self.hand))
                print(f'|{a}    |'+f'|{b}    |'+f'|{c}    |'+f'|{d}    |'+f'|{e}    |')
                print(f'|      |'*len(self.hand))
                print(f'|      |'*len(self.hand))
                print(f'|____{a}|'+f'|____{b}|'+f'|____{c}|'+f'|____{d}|'+f'|____{e}|\n')
        elif len(self.hand) == 6:
            c = self.hand[2][0][0:2]
            d = self.hand[3][0][0:2]
            e = self.hand[4][0][0:2]
            f = self.hand[5][0][0:2]
            for i in range(1):
                print(f' ______\t'*len(self.hand))
                print(f'|{a}    |'+f'|{b}    |'+f'|{c}    |'+f'|{d}    |'+f'|{e}    |'+f'|{f}    |')
                print(f'|      |'*len(self.hand))
                print(f'|      |'*len(self.hand))
                print(f'|____{a}|'+f'|____{b}|'+f'|____{c}|'+f'|____{d}|'+f'|____{e}|'+f'|____{f}|\n')   


class Player(Dealer):
    
    def __str__(self, name):
        name = self.name
        return self.name

    def __repr__(self):
        return f"Player: {self.name}"


class Hand():

    def __init__(self):
        self.hand = []

    def __str__(self):
        if self.hand == []:
            return f"This hand contains the {self.hand[0][0]} and the {self.hand[1][0]}."

    def __repr__(self):
        return f"<Cards | {self.hand[0][0]} {self.hand[1][0]}>"

    def create_hand(self):                                                  
        self.hand.append(random.choices(deck, k=1)*2)    # deals two cards to hand
        deck.remove(self.hand[-1][0])*2                  # deletes two cards from deck
        # self.hand.append(random.choices(deck, k=1))
        # deck.remove(self.hand[-1][0])
        return self.hand

    def hit(self):
        self.hand.append(random.choices(deck, k=1))
        deck.remove(self.hand[-1][0])
        print(self.hand)
        return self.hand

# main function to run game

class Game(Dealer):
    def __init__(self):

        print(intro)

        name = input("Enter your name here: ").title()
        print_cyan(f"Welcome {name} to {title}!")

        start_q = input_cyan('Do you know how to play Blackjack? Are you ready to play? (Y/N/Quit) ').lower()
        
        if start_q == 'quit':
            print_cyan(f"Thanks for visiting {title}, {name}. Come again soon!") 

        if start_q == 'n':
            clear_screen()
            print("""
            Here are the basics: 

            You are playing against the dealer. You each receive two cards to begin, however you will only see one 
            of the dealer's cards. You are trying to beat the dealer at getting 21 points or as close to it as possible
            without going over. Going over is known as a "bust." Aces are worth either one or eleven points. There are 
            no wild cards. If, one the first deal, the dealer gives you an ace and a card worth ten points (21 points), 
            you've won Black Jack! 
            
            If you do not have 21 points after the first deal, you will choose to hit (receive another card) or stand 
            (stay with the cards you have). You may hit as many times as you wish. Just be careful not to go bust! If 
            you achieve 21 points after the first deal, you win, but do not achieve Black Jack. In the event of a tie, 
            the dealer wins.
            """)
            time.sleep(5)
            clear_screen()
            print(start_q)

        while start_q not in ('y', 'n'):
            print(error)
            print(start_q)

        if start_q == 'y':
            print_cyan(figlet_format("Let's Go!", font='basic'))

            dealer = Dealer('Monty') # creating instance of Dealer
            player = Player(name)   # creating instance of Player
            again = 'y'

            print(f"Your dealer today is {name}."  )

            while again == 'y':
                if len(deck) < 25:
                    deck = full_deck[:]
                
                print("Monty is dealing...")
                time.sleep(2)

                player_hand = Hand()
                player_hand.create_hand()
                dealer_hand = Hand()
                dealer_hand.create_hand()
                player.reveal_hand(player_hand)
                dealer.hidden_hand(dealer_hand)
                player_value = player.value(player_hand.hand)

                if player_value == 21:
                    print(blackjack_win)
                    
                else:
                    print(f"Dealer's visible card: {dealer_hand.hand[1][0]}")
                    choice = input_cyan('Do you choose to Hit or Stand? (H/S) ').lower()
                    
                    while choice not in ('h', 's'):
                        print(error)
                        print(choice)
                    
                    while choice == 'h':
                        player_hand.hit()
                        player.reveal_hand(player_hand)
                        player_value = player.value(player_hand.hand)
                        
                        if player_value == 21:
                            print_yellow(figlet_format("You won!", font='basic'))
                            break
                        
                        elif player_value > 21:
                            print(bust)
                            print_red('You BUSTED! Better luck next time!')
                            break
                    
                        else:
                            print(f"Dealer's visible card: {dealer_hand.hand[1][0]}")
                            
                            decision = input('Would you like to hit again? (H/S) ').lower()
                            while decision not in ('h', 's'):
                                print(error)
                                print(decision)
                    else:
                        # if stand - determine winner
                        # show dealers cards
                        if player_value >= 21:
                            continue
                        
                        else: 
                            dealer.reveal_hand(dealer_hand)
                            dealer_value = dealer.value(dealer_hand.hand)
                            
                            while dealer_value < 17:
                                print("Monty hits the Dealer hand.")
                                dealer_hand.hit()
                                dealer.reveal_hand(dealer_hand)
                                dealer_value = dealer.value(dealer_hand.hand)
                                time.sleep(2)
                            
                            if 17 <= dealer_value <= 21:
                                if dealer_value > player_value:
                                    player.value(player_hand.hand)
                                    print_blue('Dealer wins!')

                                elif dealer_value == player_value:
                                    player.value(player_hand.hand)
                                    print_blue("It's a tie. Dealer wins!")
                                
                                else:
                                    player.value(player_hand.hand)
                                    print_yellow('You win!')
                                
                            else:
                                player.value(player_hand.hand)
                                print_yellow('Dealer BUSTED. You win!')
                                
                again = input_cyan('Would you like to play again? (Y/N) ')
                
                while again not in ('y','n'):
                    print(error)
                    print(again)
                
                if again == 'n':
                    print(f'{name}, thanks for playing {title}! Come again soon!')


if __name__ == "__main__":
    game = Game()
    game.play()