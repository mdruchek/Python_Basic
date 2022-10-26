import random

class Cell:
    def __init__(self, is_busy, number):
        self.number = number
        self.is_busy = is_busy

    def return_is_busy(self):
        return self.is_busy

    def change_state(self, state):
        if self.return_is_busy() in '123456789':
            self.is_busy = state
        else:
            raise ValueError

class Board:
    def __init__(self):
        self.board = [Cell(str(number), number) for number in range(1, 10)]

    def return_cell_is_busy(self, number):
        return self.board[number].is_busy

    def print_board(self):
        for i_cell, cell in enumerate(self.board):
            print(' {}'.format(self.return_cell_is_busy(i_cell)), end='')
            if (i_cell + 1) % 3 == 0:
                 print()

    def change_state_cell(self, number, is_busy):
        self.board[number].change_state(is_busy)

    def get_board_condition(self, busy):
        busy_set = set()
        for number_cell in range(9):
            if self.return_cell_is_busy(number_cell) in busy:
                busy_set.add(number_cell)
        return busy_set


class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer

    def make_move(self, board=None):
        if self.is_computer:
            free_cell = list(board.get_board_condition('123456789'))
            move = free_cell[random.randint(0, len(free_cell) - 1)]
        else:
            move = int(input()) - 1
        return move

    def get_name(self):
        return self.name


class TicTacToeGame:
    winning_combinations = [{0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 4, 8}, {2, 4, 6}]

    def __init__(self, name1, name2, player2_is_computer):
        self.board = Board()
        self.player1 = Player(name1)
        self.player2 = Player(name2, player2_is_computer)
        self.players = [self.player1, self.player2]

    def who_goes_first(self):
        first_player = random.randint(0, 1)
        if first_player == 1:
            self.players.reverse()
        print('Первым ходит {}.'.format(self.players[0].get_name()))

    def request_player_move(self, player):
        print('Ход {}: '.format(player.get_name()), end='')
        if player.is_computer:
            print()
            return player.make_move(self.board)
        else:
            return player.make_move()

    def change_state_cell_board(self, number, is_busy):
        self.board.change_state_cell(number, is_busy)

    def get_board_condition(self, busy):
        return self.board.get_board_condition(busy)

    def is_game_over(self, busy):
        occupied_cells = self.get_board_condition(busy)
        for win_condition in self.winning_combinations:
            if win_condition <= occupied_cells:
                return True
        return False

    def is_draw(self):
        free_cell = self.get_board_condition('123456789')
        if len(free_cell) == 0:
            return True
        return False

    def game(self):
        self.who_goes_first()
        print('Вместо пустых клеток стоит номер хода.')
        self.board.print_board()
        game_over = False
        is_draw = False
        while True:
            for i_sym, symbol in enumerate('XO'):
                try:
                    self.change_state_cell_board(self.request_player_move(self.players[i_sym]), symbol)
                except ValueError:
                    print('Эта клетка занята!')
                    self.change_state_cell_board(self.request_player_move(self.players[i_sym]), symbol)
                self.board.print_board()
                if self.is_game_over(symbol):
                    name_win = self.players[i_sym].get_name()
                    game_over = True
                    is_draw = False
                    break
                if self.is_draw():
                    game_over = True
                    is_draw = True
                    break
            if game_over:
                break
        if is_draw:
            print('Ничья!')
        else:
            print('Победил {}!'.format(name_win))
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