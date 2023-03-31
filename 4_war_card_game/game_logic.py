import card_class

""" Game Set-up """

player_one = card_class.Player("One")
player_two = card_class.Player("Two")

new_deck = card_class.Deck()
new_deck.shuffle_deck()

for card in range(26):
    """Deal half the deck to each player"""
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_number = 0

while game_on:
    
    """Game Start"""

    round_number += 1
    print(f"Round: {round_number}")

    """ Check for wins """

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two WINS!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two is out of cards! Player One WINS!")
        game_on = False
        break

    """New Rounds"""
    player_one_cards = []
    # This takes a card from the dealt list 
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    # This takes a card from the dealt list 
    player_two_cards.append(player_two.remove_one())

    """Second while loop for specific game logic (War)"""

    at_war = True

    while at_war:
        # Player one wins the cards
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        # Player two wins the cards
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else: 
            print("WAR!!")

            if len(player_one.all_cards) < 5:
                print("Player One unable to go to war!")
                print("Player Two WINS!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to go to war!")
                print("Player One WINS!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())