import random

class Cell:
    def __init__(self, is_busy, number):
        self.number = number
        self.is_busy = is_busy

    def return_is_busy(self):
        return self.is_busy

    def change_state(self, state):
        if self.return_is_busy() == '-':
            self.is_busy = state

class Board:
    def __init__(self):
        self.board = [Cell('-', number) for number in range(1, 10)]

    def return_cell_is_busy(self, number):
        return self.board[number].is_busy

    def print_board(self):
        for i_cell, cell in enumerate(self.board):
            print(' {}'.format(self.return_cell_is_busy(i_cell)), end='')
            if (i_cell + 1) % 3 == 0:
                 print()

    def change_state_cell(self, number, is_busy):
        self.board[number].change_state(is_busy)


class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer

    def make_move(self, board = None):
        if self.is_computer:
            if board.return_cell_is_busy(4) == '-':
                move = 4
        else:
            move = int(input()) - 1
        return move


class TicTacToeGame:

    def __init__(self, name1, name2, player2_is_computer):
        self.board = Board()
        self.player1 = Player(name1)
        self.player2 = Player(name2, player2_is_computer)
        self.players = [self.player1, self.player2]
        self.cross = set()
        self.zero = set()

    def who_goes_first(self):
        first_player = random.randint(0, 1)
        if first_player == 1:
            self.players.reverse()
        print('Первым ходит {}.'.format(self.players[0].name))

    def request_player_move(self, player):
        if player.is_computer:
            return player.make_move(self.board)
        else:
            print('Ход {}:'.format(player.name))
            return player.make_move()

    def change_state_cell_board(self, number, is_busy):
        self.board.change_state_cell(number, is_busy)

    def is_game_over(self):
        return True

    def game(self):
        self.who_goes_first()
        while self.is_game_over():
            self.change_state_cell_board(self.request_player_move(self.players[0]), 'X')
            self.board.print_board()
            self.change_state_cell_board(self.request_player_move(self.players[1]), '0')
            self.board.print_board()


print('Игра "Крестики-нолики"')
number_players = int(input('Введите количество игроков (1 или 2): '))

if number_players == 1:
    player1_name = input('Введите имя: ')
    player2_name = 'Компьютер'
    player2_is_computer = True

if number_players == 2:
    player1_name = input('Введите имя первого игрока: ')
    player2_name = input('Введите имя второго игрока: ')
    player2_is_computer = False

tic_tac_toe = TicTacToeGame(player1_name, player2_name, player2_is_computer)
tic_tac_toe.game()