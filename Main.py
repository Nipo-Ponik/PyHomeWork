from colorama import Fore, Back
from random import randint


class Card():
    def __init__(self, rank: str, color: bool, suit):
        self.rank = rank
        self.color = color
        self.suit = suit

    def get(self):
        return self.rank, self.suit, self.color

def generation():
    cards = []
    RANKS = ['6', '7', '8', '9', '10', '11', 'JACK', 'QUEEN', 'KING', 'ACE', 'min']  # очки/наминал карты по индексу, всего 9
    SUITS = ['pikes', 'clovers', 'tiles', 'hearts']
    for i in range(36):
        cards.append(Card(str(RANKS[randint(0, len(RANKS)-1)]), randint(0, 1), 'none'))
        if cards[i].color: # 1 - чёрный цвет, 0 - красный
            cards[i].suit = SUITS[randint(0, 1)]
        else:
            cards[i].suit = SUITS[randint(2, 3)]
    return cards


def check_cards(cards):
    out = []
    for k in range(36):
        for i in range(36):
            if k != i and cards[k] == cards[i]:
                out.append(i)
    if len(out) == 0:
        return 'None'
    else:
        return out


def print_cards(cards: list, n=6, debug=False):
    out = []
    for i in range(n):
        out.append(cards.pop(randint(0, len(cards)-1)).get())
        if out[i][2]:
            print(Fore.LIGHTBLACK_EX + str(out[i][0]) + ' ' + out[i][1])
        else:
            print(Fore.RED + out[i][0] + ' ' + out[i][1])

    if debug:
        print(Fore.RESET + '\nCards left: ')
        for i in range(36-n):
            print(cards[i].get())


def add_card(deck, amount=1):
    add_cards = []
    for i in range(amount):
        add_cards.append(deck.pop(randint(0, len(deck)-1)))
    return add_cards, deck


RANKS = ['6', '7', '8', '9', '10', '11', 'JACK', 'QUEEN', 'KING', 'ACE', 'min'] # очки/наминал карты по индексу, всего 9
SUITS = ['pikes', 'clovers', 'tiles', 'hearts']

deck = generation()

player_cards = list(add_card(deck, 6))
deck = player_cards[1]
player_cards = player_cards[0]

enemy_cards = list(add_card(deck, 6))
deck = enemy_cards[1]
enemy_cards = enemy_cards[0]

if input('Press Enter for start') == 'd':
    print('Player cards:')
    print_cards(player_cards, len(player_cards))
    print()
    print('Enemy cards:')
    print_cards(enemy_cards, len(enemy_cards))
    print()
    print('Cards:')
    print_cards(deck, len(deck))


while(True):
    print('Player cards:')
    print_cards(player_cards, len(player_cards))
    print()

    table = [[], []]
    card = Card(RANKS[10], 0, SUITS[3]) # максимум очков/ранг карт 9

    # for c in enemy_cards:
    #    print_cards([c], 1)
    #    print(c.rank)
    #    if RANKS.index(c.rank) < RANKS.index(card.rank):
    #        card = c
    #
    # table[0].append(enemy_cards.pop(RANKS.index(card.rank)))
    # print_cards(table, 1)
    break


# debug = 0
# if debug:
#     print('Coincidences: ' + check_cards(deck))

# print_cards(deck, debug=debug)
