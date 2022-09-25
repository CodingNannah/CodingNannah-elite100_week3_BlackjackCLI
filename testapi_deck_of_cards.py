import requests
url_doc = 'https://www.deckofcardsapi.com/'
response = requests.get(url_doc)
data = response.json()
print(response)

# shuffle cards: https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1 
    # add deck_count as a GET or POST parameter to define the number of decks
    # Blackjack usually uses 6, default 1
# draw a card: https://www.deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2
    # replace <<deck_id>> with valid deck_id or with 'new' to create a shuggled deck AND draw cards in the same request
# new deck: https://www.deckofcardsapi.com/api/deck/new/
# add to piles: https://www.deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/add/?cards=AS,2S 
    # Piles can be used for discarding, players hands, or whatever else. Piles are created on the fly, just give a pile a name and add a drawn card to the pile. If the pile didn't exist before, it does now. After a card has been drawn from the deck it can be moved from pile to pile.
    # Note: This will not work with multiple decks.
# listing cards in piles: https://www.deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/list/
    # Note: This will not work with multiple decks.


#json decode errors:
#line 355 in raw_decode:
#json.decoder..JSONDecodeERROR: Expecting value: line 8 column 1 (char 7)
#line 975 in json:
#requests.exceptions.JSONDecodeERROR: Expecting value: line 8 column 1 (char 7)