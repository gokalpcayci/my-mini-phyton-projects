import random

# Define the ranks and suits of a standard deck of cards
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Define the values of each rank (aces can be 1 or 11)
card_values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

# Define a function to create a new deck of cards
def new_deck():
    deck = []
    for rank in ranks:
        for suit in suits:
            card = rank + ' of ' + suit
            deck.append(card)
    random.shuffle(deck)
    return deck

# Define a function to deal a card from the deck
def deal_card(deck):
    card = deck.pop()
    return card, card_values[card.split()[0]]

# Define a function to calculate the total value of a hand
def hand_value(hand):
    total = sum(card_values[card.split()[0]] for card in hand)
    num_aces = hand.count('Ace of Hearts') + hand.count('Ace of Diamonds') + hand.count('Ace of Clubs') + hand.count('Ace of Spades')
    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1
    return total

# Define the main game function
def play_game():
    print('Welcome to Blackjack!')
    deck = new_deck()
    player_hand = []
    dealer_hand = []
    player_hand.append(deal_card(deck)[0])
    dealer_hand.append(deal_card(deck)[0])
    player_hand.append(deal_card(deck)[0])
    dealer_hand.append(deal_card(deck)[0])
    print('Your hand:', player_hand)
    print('Dealer shows:', dealer_hand[0])
    while True:
        choice = input('Hit or stand? ')
        if choice.lower() == 'hit':
            player_hand.append(deal_card(deck)[0])
            print('Your hand:', player_hand)
            if hand_value(player_hand) > 21:
                print('Bust! You lose.')
                return
        elif choice.lower() == 'stand':
            break
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck)[0])
    print('Your hand:', player_hand)
    print('Dealer hand:', dealer_hand)
    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)
    if player_total > 21:
        print('Bust! You lose.')
    elif dealer_total > 21:
        print('Dealer busts! You win.')
    elif player_total > dealer_total:
        print('You win!')
    elif player_total < dealer_total:
        print('Dealer wins!')
    else:
        print('Push.')

# Play the game
while True:
    play_game()
    choice = input('Play again? (y/n) ')
    if choice.lower() != 'y':
        break
