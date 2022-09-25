import time
from colorizer import clear_screen
import ascii_magic

ascii_magic.init_terminal()

def intro(self, cols=100):
    clear_screen()
    print('\n *5')
    url = "https://www.pngmart.com/image/32119"
    welcome_img = ascii_magic.from_url(self.image, columns=cols)
    ascii_magic.to_terminal(welcome_img)
    time.sleep(2)
    clear_screen()

    blackjack_img = ascii_magic.from_image_file('./images/blackjack_icon.png')
    ascii_magic.to_terminal(blackjack_img)
    time.sleep(2)
    clear_screen()
    
    return intro


def blackjack_win(self, cols=100):   
    clear_screen()
    print('\n *5')
    fireworks_img = ascii_magic.from_image_file('./images/fireworks.png')
    ascii_magic.to_terminal(fireworks_img)
    time.sleep(2)
    clear_screen()

    win_img = ascii_magic.from_image_file('./images/blackjack.png')
    ascii_magic.to_terminal(win_img)
    time.sleep(2)
    clear_screen()  
    
    return blackjack_win


def bust(self, cols=100):   
    clear_screen()
    print('\n *5')
    explode_img = ascii_magic.from_image_file('./images/explode.png')
    ascii_magic.to_terminal(explode_img)
    time.sleep(2)
    clear_screen()

    bust_img = ascii_magic.from_image_file('./images/bust.png')
    ascii_magic.to_terminal(bust_img)
    time.sleep(2)
    clear_screen()

    return blackjack_win
