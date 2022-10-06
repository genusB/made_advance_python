import sys
import unittest
import io
from unittest.mock import patch
import tic_tac_game


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.game = tic_tac_game.TicTacGame()
        self.player1_win_set = ['X', 'X', 'X']
        self.player2_win_set = ['0', '0', '0']

    def test_player_change(self):
        self.assertEqual(self.game.current_player, self.game.players[0])

        self.game.moves += 1
        self.game.change_player()
        self.assertEqual(self.game.current_player, self.game.players[1])

        self.game.moves += 1
        self.game.change_player()
        self.assertEqual(self.game.current_player, self.game.players[0])

    fake_correct_input = iter(['1', '1', '2', '2']).__next__

    @patch('builtins.input', fake_correct_input)
    def test_move(self):
        self.game.make_move()
        self.assertEqual(self.game.board[0][0], 'X')

        self.game.change_player()

        self.game.make_move()
        self.assertEqual(self.game.board[1][1], '0')

    def test_correct_input(self):
        self.assertEqual(self.game.is_correct_input('1', '1'), True)
        self.assertEqual(self.game.is_correct_input('2', '2'), True)

        self.game.moves += 1
        self.game.change_player()

        self.assertEqual(self.game.is_correct_input('2', '1'), True)
        self.assertEqual(self.game.is_correct_input('1', '2'), True)

    @patch('builtins.print')
    def test_pass_coordinates_incorrectly(self, mock_print):
        self.assertEqual(self.game.is_correct_input('1 1', '1 1'), False)
        mock_print.assert_called_with('Coordinates must be integer numbers')

        self.assertEqual(self.game.is_correct_input('a', 'a'), False)
        mock_print.assert_called_with('Coordinates must be integer numbers')

        self.assertEqual(self.game.is_correct_input('1.2', '2.3'), False)
        mock_print.assert_called_with('Coordinates must be integer numbers')

    @patch('builtins.print')
    def test_coordinates_out_of_range(self, mock_print):
        self.assertEqual(self.game.is_correct_input('4', '3'), False)
        mock_print.assert_called_with('Coordinates must be in range from 1 to 3')

        self.assertEqual(self.game.is_correct_input('3', '4'), False)
        mock_print.assert_called_with('Coordinates must be in range from 1 to 3')

    fake_correct_input = iter(['1', '1', '2', '2']).__next__

    @patch('builtins.input', fake_correct_input)
    @patch('builtins.print')
    def test_coordinates_is_busy(self, mock_print):
        self.game.make_move()
        self.assertEqual(self.game.is_correct_input('1', '1'), False)
        mock_print.assert_called_with('This cell is already busy. Choose another one')

        self.game.change_player()

        self.game.make_move()
        self.assertEqual(self.game.is_correct_input('2', '2'), False)
        mock_print.assert_called_with('This cell is already busy. Choose another one')

    fake_win_input = iter(['1', '1', '1', '2', '2', '1', '2', '2', '3', '1']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player1_by_first_column(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player1 is the winner!')
        self.assertListEqual([self.game.board[0][0], self.game.board[1][0], self.game.board[2][0]], self.player1_win_set)

    fake_win_input = iter(['1', '2', '1', '1', '2', '2', '2', '1', '3', '2']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player1_by_second_column(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player1 is the winner!')
        self.assertListEqual([self.game.board[0][1], self.game.board[1][1], self.game.board[2][1]], self.player1_win_set)

    fake_win_input = iter(['1', '3', '1', '2', '2', '3', '2', '2', '3', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player1_by_third_column(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player1 is the winner!')
        self.assertListEqual([self.game.board[0][2], self.game.board[1][2], self.game.board[2][2]], self.player1_win_set)

    fake_win_input = iter(['1', '1', '2', '1', '1', '2', '2', '2', '1', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player1_by_first_row(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player1 is the winner!')
        self.assertListEqual(self.game.board[0][0:3], self.player1_win_set)

    fake_win_input = iter(['2', '1', '1', '1', '2', '2', '1', '2', '2', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player1_by_second_row(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player1 is the winner!')
        self.assertListEqual(self.game.board[1][0:3], self.player1_win_set)

    fake_win_input = iter(['3', '1', '2', '1', '3', '2', '2', '2', '3', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player1_by_third_row(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player1 is the winner!')
        self.assertListEqual(self.game.board[2][0:3], self.player1_win_set)

    fake_win_input = iter(['1', '1', '1', '2', '2', '2', '2', '3', '3', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player1_by_first_diagonal(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player1 is the winner!')
        self.assertListEqual([self.game.board[0][0], self.game.board[1][1], self.game.board[2][2]], self.player1_win_set)

    fake_win_input = iter(['1', '3', '1', '2', '2', '2', '2', '1', '3', '1']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player1_by_second_diagonal(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player1 is the winner!')
        self.assertListEqual([self.game.board[0][2], self.game.board[1][1], self.game.board[2][0]], self.player1_win_set)

    # ------------
    fake_win_input = iter(['1', '3', '1', '1', '1', '2', '2', '1', '2', '2', '3', '1']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player2_by_first_column(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player2 is the winner!')
        self.assertListEqual([self.game.board[0][0], self.game.board[1][0], self.game.board[2][0]], self.player2_win_set)

    fake_win_input = iter(['1', '3', '1', '2', '1', '1', '2', '2', '2', '1', '3', '2']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player2_by_second_column(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player2 is the winner!')
        self.assertListEqual([self.game.board[0][1], self.game.board[1][1], self.game.board[2][1]], self.player2_win_set)

    fake_win_input = iter(['1', '1', '1', '3', '1', '2', '2', '3', '2', '2', '3', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player2_by_third_column(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player2 is the winner!')
        self.assertListEqual([self.game.board[0][2], self.game.board[1][2], self.game.board[2][2]], self.player2_win_set)

    fake_win_input = iter(['3', '1', '1', '1', '2', '1', '1', '2', '2', '2', '1', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player2_by_first_row(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player2 is the winner!')
        self.assertListEqual(self.game.board[0][0:3], self.player2_win_set)

    fake_win_input = iter(['3', '1', '2', '1', '1', '1', '2', '2', '1', '2', '2', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player2_by_second_row(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player2 is the winner!')
        self.assertListEqual(self.game.board[1][0:3], self.player2_win_set)

    fake_win_input = iter(['1', '1', '3', '1', '2', '1', '3', '2', '2', '2', '3', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player2_by_third_row(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player2 is the winner!')
        self.assertListEqual(self.game.board[2][0:3], self.player2_win_set)

    fake_win_input = iter(['1', '3', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player2_by_first_diagonal(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player2 is the winner!')
        self.assertListEqual([self.game.board[0][0], self.game.board[1][1], self.game.board[2][2]], self.player2_win_set)

    fake_win_input = iter(['1', '1', '1', '3', '1', '2', '2', '2', '2', '1', '3', '1']).__next__

    @patch('builtins.input', fake_win_input)
    @patch('builtins.print')
    def test_win_player2_by_second_diagonal(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Player2 is the winner!')
        self.assertListEqual([self.game.board[0][2], self.game.board[1][1], self.game.board[2][0]], self.player2_win_set)

    fake_draw_input = iter(['1', '1', '1', '3', '1', '2', '2', '1', '2', '3', '2', '2', '3', '1', '3', '2', '3', '3']).__next__

    @patch('builtins.input', fake_draw_input)
    @patch('builtins.print')
    def test_draw(self, mock_print):
        self.game.start_game()
        self.game.is_game_over()
        mock_print.assert_called_with('Draw!')
        self.assertEqual(self.game.moves, 9)

if __name__ == "__main__":
    unittest.main()
