'''
Tic Tac Toe unit tests
'''
import unittest
import tic_tac_toe

class TestTicTacToe(unittest.TestCase):
    '''
    Class to test the functions
    '''
    def setUp(self):
        '''
        Setup function is called before each test
        '''
        self.grid = [['X', 'X', 'X'], [' ', ' ', 'X'], [' ', ' ', 'X']]

    def test_check_row_is_true(self):
        '''
        Test that the check row returns true
        '''
        row = 0
        player = 'X'

        result = tic_tac_toe.check_row(self.grid, row, player)
        self.assertEqual(result, True)

    def test_check_row_is_false(self):
        '''
        Test that the check row returns false
        '''
        row = 2
        player = 'X'

        result = tic_tac_toe.check_row(self.grid, row, player)
        self.assertEqual(result, False)

    def test_check_column_is_true(self):
        '''
        Test that the check column returns true
        '''
        grid = [['O', 'X', 'X'], ['O', ' ', ' '], ['O', ' ', ' ']]
        column = 0
        player = 'O'

        result = tic_tac_toe.check_column(grid, column, player)
        self.assertEqual(result, True)

    def test_check_column_is_false(self):
        '''
        Test that the check column returns false
        '''
        column = 2
        player = 'O'

        result = tic_tac_toe.check_column(self.grid, column, player)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
