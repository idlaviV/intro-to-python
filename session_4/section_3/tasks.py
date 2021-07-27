# A bit bigger task:
# try to programm a very basic version of a card game:
# using a french deck (make_french_deck) 
# RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# SUITS = ['Hearts', 'Spades', 'Diamonds', 'Clubs'] # Herz, Pik, Karo, Kreuz

# implement two classes: a game class where we can pass the number of players
# according to that number we then create a list of players
# a game also has a deck of cards which needs to be shuffled
# implement a deal_cards method which deals every player 5 cards,
# furthrt a play_round method where each player is displayed his current cards
# and the player can choose the card (s)he wants to play
# finally determine the winner of this round using the rank of the cards

# the second class is a player class. every player has some cards (card_objectcs)
# (s)he has also a number of points and potentially a position on the table
# and maybe a boolean value encoding if it is his/her turn

# you can also introduce a third class - a dealer class

# in the card_deck.py file are already two classes: CARD, DECK and one function:
# make_french_deck() which returns a DECK object which is basically 
# a list of card CARD objectcs

# import everything from the card_deck.py file using the wildcard import
# we can now access everything as if it would be all in one file
from card_deck import *