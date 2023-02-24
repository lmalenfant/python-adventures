def player_selection():
    choice = ' '
    
    while choice not in ['x', 'X', 'o', 'O']:
        choice = input('Player 1, would you like O or X? ')
        
        if choice not in ['x', 'X', 'o', 'O']:
            print('Oops, that is not a valid choice, Please select O or X: ')
    
    return choice.upper()


def print_board(grid):
    print(' '*3)
    print(f' {grid[0][0]} | {grid[0][1]} | {grid[0][2]} ')
    print(f'___________')
    print(f' {grid[1][0]} | {grid[1][1]} | {grid[1][2]} ')
    print(f'___________')
    print(f' {grid[2][0]} | {grid[2][1]} | {grid[2][2]} ')
    print(' '*3)


def position_selection(player):
    choice = ' '
    in_range = False
    
    while choice.isdigit() == False or in_range == False:
        choice = input(f"Player '{player}' Select a position from the grid (0-9): ")
        
        if choice.isdigit():
            if int(choice) in range(1,10):
                in_range = True
            else:
                print('Please enter a number in the range (1 - 9)')
                in_range = False
        else:    
            print('Please enter a valid number')
            
    return int(choice)


def is_winning_move(grid, position, player):
    position_dictionary = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 9: [2,2]}

    row = position_dictionary[position][0]
    column = position_dictionary[position][1]
    
    if check_row(grid, row, player):
        print('row wins')
        return True
    if check_column(grid, column, player):
        print('column wins')
        return True
    if position in [1,3,5,7,9]:
        if check_diagonal(grid, player):
            print('diagonal wins')
            return True
    return False

def write_value(grid, position, player):    
    if position in [1, 2, 3]:
            grid[0][position-1] = player
    if position in [4, 5, 6]:
            grid[1][position-4] = player
    if position in [7, 8, 9]:
            grid[2][position-7] = player

    #check to see if the last move was a winning move
    winning_move = is_winning_move(grid, position, player)
            
    print_board(grid)
    return winning_move

def check_position(grid, position):
    row = ''
    column = ''
    
    if position in [1, 2, 3]:
        row = 0
        column = position-1
    elif position in [4, 5, 6]:
        row = 1
        column = position-4
    elif position in [7, 8, 9]:
        row = 2
        column = position-7
    else:
        return 'Invalid position'
    return grid[row][column] == ' '

def check_full_board(grid):
    for row in grid:
        for position in row:
            if position == ' ':
                return False
    return True

def check_row(grid, row, player):
    if grid[row][0] == player and grid[row][1] == player and grid[row][2] == player:
        return True
    return False

def check_column(grid, column, player):
    if grid[0][column] == player and grid[1][column] == player and grid[2][column] == player:
        return True    
    return False

def check_diagonal(grid, player):
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True        
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True        
    return False

def replay():
    choice = ' '
    
    while choice not in ['y', 'Y', 'n', 'N']:
        choice = input('Would you like to play again? Y or N: ')
        
        if choice not in ['y', 'Y', 'n', 'N']:
            print('Oops, that is not a valid choice, Please select Y or N: ')
    
    return choice.upper() == 'Y'

import os
clear = lambda: os.system('cls') #on Windows System
template_grid = [[1, 2, 3], [4, 5,6], [7,8, 9]]
keep_playing = True
while keep_playing:
    clear()
    print('Welcome to TIC TAC TOE!')
    game_in_progress = True
    full_board = False
    game_grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    #Let player 1 select O or X
    player = player_selection()

    while game_in_progress:
        #check to see if the board is full
        if check_full_board(game_grid):
            print('Nobody wins this one!')
            full_board = True
            game_in_progress = False
        else:
            print_board(template_grid)

            position = position_selection(player)
            while not check_position(game_grid, position) and not full_board:
                print('That position is already filled please select another')
                position = position_selection(player)

            clear()
            win = write_value(game_grid, position, player)
            if win:
                print(f'Congratulations {player}! You win')
                game_in_progress = False
            else:
                #next player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                    
    keep_playing = replay()
