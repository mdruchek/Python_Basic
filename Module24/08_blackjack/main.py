import random


class Card:
    weights = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}

    def __init__(self, suit, weight):
        self.suit = suit
        self.weight = weight

    def weight_return(self):
        return self.weights[self.weight]

    def return_card(self):
        return self.weight, self.suit


class Deck:
    suits = ['Червы', 'Бубны', 'Пики', 'Крести']
    weights = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

    def __init__(self):
        self.deck_cards = [Card(suit, weight) for suit in self.suits for weight in self.weights]

    def hand_over_card(self):
        number_card = random.randint(0, len(self.deck_cards) - 1)
        card_to_be_dealt = self.deck_cards[number_card]
        self.deck_cards.remove(card_to_be_dealt)
        return card_to_be_dealt


class Player:
    def __init__(self, name):
        self.name = name
        self.cards_on_hand = []

    def take_card(self, card):
        self.cards_on_hand.append(card)

    def return_weight_cards(self):
        weight_card = []
        for card in self.cards_on_hand:
            weight_card.append(card.weight_return())
        if sum(weight_card) > 21:
            for index, weight in enumerate(weight_card):
                if weight == 11:
                    weight_card[index] = 1
                if sum(weight_card) < 21:
                    break
        return sum(weight_card)

    def print_cards(self):
        for card in self.cards_on_hand:
            weight, suit = card.return_card()
            print('{} {}'.format(weight, suit))


customization_computer = 18 #до скольки очков компьютер берёт карту
winner = None
loser = None

print('Игра "Блек_джек":')
name = input('Введите имя: ')
deck = Deck()
player = Player(name)
computer = Player('Компьютер')

for _ in range(2):
    player.take_card(deck.hand_over_card())
    computer.take_card(deck.hand_over_card())
player.print_cards()

hand_over_player_flag = True
hand_over_computer_flag = True
draw_flag = False

while True:
    if hand_over_player_flag:
        question = input('Сдать ещё? ').lower()
        if question == 'да':
            player.take_card(deck.hand_over_card())
            player.print_cards()
            if player.return_weight_cards() > 21:
                winner = computer
                loser = player
                break
        else:
            hand_over_player_flag = False

    if computer.return_weight_cards() <= customization_computer:
        computer.take_card(deck.hand_over_card())
        if computer.return_weight_cards() > 21:
            winner = player
            loser = computer
            break
    else:
        hand_over_computer_flag = False

    if not hand_over_player_flag and not hand_over_computer_flag:
        if computer.return_weight_cards() > player.return_weight_cards():
            winner = computer
            loser = player
            break
        elif player.return_weight_cards() > computer.return_weight_cards():
            winner = player
            loser = computer
            break
        else:
            draw_flag = True
            break

if draw_flag:
    print('Ничья! ({} : {})'
          .format(player.name, winner.return_weight_cards(), computer.return_weight_cards()))
# print('--{}--'.format(computer.name))
# computer.print_cards()
# print('------------')
print('{} победил! ({} : {})'
      .format(winner.name, winner.return_weight_cards(), loser.return_weight_cards()))
