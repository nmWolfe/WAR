import random
import pathlib

""" Global Variables for use in classes"""

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
        'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:

    """ a simple class to model a card and return info when called """

    def __init__(self,suit,rank):
        """ Initialize the Card Class """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        """ Represents the card obj as a string """
        return self.rank + " of " + self.suit

class Deck:

    """ A Class to create a deck of cards from the Card class """

    def __init__(self):
        """ Initializing the Deck """
        self.all_cards = []
        """ This will pull from the global variables Suits and Ranks
        and run them through the Card class to create the full deck
        """
        for suit in suits:
            for rank in ranks:
                # Create a card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        """ Shuffle the deck """
        random.shuffle(self.all_cards)

    def deal_one(self):
        """ Return a single card """
        return self.all_cards.pop()

class Player:

    """ A class to model a player in a game of cards """

    def __init__(self,name):
        """ Initialize """
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """ Remove a card from the 'top' of the list """
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        """ Adding cards to the players hand """
        if type(new_cards) == type([]):
            # Multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # Single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

path = pathlib.Path('READ_ME.txt')

contents = path.write_text("""
This is a game of the card game WAR, simulated by two AI players. 

The goal is to be the first player to win all 52 cards

The Deal

The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. Anyone may deal first. Each player places their stack of cards face down, in front of them.

The Play

Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack.

If the cards are the same rank, it is War. Each player turns up one card face down and one card face up. The player with the higher cards takes both piles (six cards). If the turned-up cards are again the same rank, each player places another card face down and turns another card face up. The player with the higher card takes all 10 cards, and so on.

How to Keep Score

The game ends when one player has won all the cards.
""")

