class TicTacGame:

    def __init__(self):
        self.board = [['.', '.', '.'] for _ in range(3)]
        self.players = [('Player1', 'X'), ('Player2', '0')]
        self.current_player = self.players[0]
        self.moves = 0

    def show_board(self):
        for row in self.board:
            print(*row)

    def is_correct_input(self, x_pos, y_pos):
        if not x_pos.isdigit() or not y_pos.isdigit():
            print('Coordinates must be integer numbers')
            return False
        else:
            x_pos = int(x_pos) - 1
            y_pos = int(y_pos) - 1
        if not 0 <= x_pos < 3 or not 0 <= y_pos < 3:
            print('Coordinates must be in range from 1 to 3')
            return False
        if not self.board[x_pos][y_pos] == '.':
            print('This cell is already busy. Choose another one')
            return False

        return True

    def make_move(self):
        print(f'{self.current_player[0]} please input x_pos and y_pos coordinates in two lines:')

        x_pos = input()
        y_pos = input()

        while not self.is_correct_input(x_pos, y_pos):
            print(f'{self.current_player[0]} please input x_pos and y_pos coordinates in two lines:')

            x_pos = input()
            y_pos = input()

        x_pos = int(x_pos) - 1
        y_pos = int(y_pos) - 1
        self.board[x_pos][y_pos] = self.current_player[1]
        self.moves += 1

    def change_player(self):
        self.current_player = self.players[self.moves % 2]

    def start_game(self):
        while not self.is_game_over():
            self.show_board()
            self.change_player()
            self.make_move()

    def is_game_over(self):
        target_symbol = [self.current_player[1], self.current_player[1], self.current_player[1]]
        conditions_to_win = []

        conditions_to_win.append(self.is_equal(self.board[0][0:3], target_symbol))
        conditions_to_win.append(self.is_equal(self.board[1][0:3], target_symbol))
        conditions_to_win.append(self.is_equal(self.board[2][0:3], target_symbol))

        board_columns = list(zip(*self.board))

        conditions_to_win.append(self.is_equal(board_columns[0][0:3], target_symbol))
        conditions_to_win.append(self.is_equal(board_columns[1][0:3], target_symbol))
        conditions_to_win.append(self.is_equal(board_columns[2][0:3], target_symbol))

        conditions_to_win.append(self.is_equal([self.board[0][0], self.board[1][1], self.board[2][2]], target_symbol))
        conditions_to_win.append(self.is_equal([self.board[0][2], self.board[1][1], self.board[2][0]], target_symbol))

        if any(conditions_to_win):
            print(f'{self.current_player[0]} is the winner!')
            return True

        if self.moves == 9:
            print('Draw!')
            return True

        return False

    @staticmethod
    def is_equal(seq1, seq2):
        if len(seq1) != len(seq2):
            return False
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                return False

        return True


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
