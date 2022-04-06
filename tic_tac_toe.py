def display_board(board):
    print(f'{board[1]}|{board[2]}|{board[3]}')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print(f'{board[7]}|{board[8]}|{board[9]}')
    return board

def choose_x_or_o():
    marker = 'Wrong'
    while marker not in ['X','O','x','o']:
        marker = input('Player 1, Please choose X or O:')
        player1 = marker.upper()
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    return [player1, player2]

def select_position(player_name):
    position = 0 
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input(player_name+' Please select the position:')
        if position not in range(1,10):
            print('Invalid input. Please select again.')
    return int(position)

def replace_and_display_board(board, position, player):
    board[position] = player
    display_board(board)
    return board

def check_winner(board, winner_set):
    win = False
    for set_combination in winner_set:
        retrive_value = f'{board[set_combination[0]]}{board[set_combination[1]]}{board[set_combination[2]]}'
        if(retrive_value in ['XXX','OOO']):
            win = True
            break
    return win

def start_game(board, player1_marker, player2_marker, winner_set):
    player_name = ''
    player_marker = 0
    counter = 1
    winner = ''
    
    while counter <= 9:
        if(counter%2 == 0):
            player_name = 'Player 2'
            player_marker = player2_marker            
        else:
            player_name = 'Player 1'
            player_marker = player1_marker

        position = select_position(player_name)
        replaced_board = replace_and_display_board(board, position, player_marker)
        
        if(counter >= 5):
            if(check_winner(replaced_board, winner_set)):
                winner = player_name
                print('Congratulations!!!', player_name, 'is the winner.')
                break
        counter+=1

    if winner == '':
        print('Oops!! Nobody wins the game.')
    return True

range_is = ['#','1','2','3','4','5','6','7','8','9']
board = display_board(range_is)

player1, player2 = choose_x_or_o()
print(f'Player 1: {player1}')
print(f'Player 2: {player2}')
print('Lets Begin The Game!')

winner_set = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
start_game(board, player1, player2, winner_set)