import os
import random

clear = lambda: os.system('cls')
def display_board(board):
    clear()
    
    print('   |   |')
    print(board[7]+'  | '+board[8]+' | '+board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(board[4]+'  | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(board[1]+'  | '+board[2]+' | '+board[3])
    print('   |   |')
    print('-----------')

def player_input():
        user_input=''
        while not (user_input == 'X' or user_input == 'O'):
            user_input = input('Do you want to be X or O? ').upper()

        if user_input == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

def place_marker(board,user_input,position):
    board[position]=user_input

def win_check(board, user_input):
    return ((board[7] == user_input and board[8] == user_input and board[9] == user_input) or # across the top
            (board[4] == user_input and board[5] == user_input and board[6] == user_input) or # across the middle
            (board[1] == user_input and board[2] == user_input and board[3] == user_input) or # across the bottom
            (board[7] == user_input and board[4] == user_input and board[1] == user_input) or # down the middle
            (board[8] == user_input and board[5] == user_input and board[2] == user_input) or # down the middle
            (board[9] == user_input and board[6] == user_input and board[3] == user_input) or # down the right side
            (board[7] == user_input and board[5] == user_input and board[3] == user_input) or # diagonal
            (board[9] == user_input and board[5] == user_input and board[1] == user_input)) # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player2'
    else:
        return 'Player1'

def space_check(board, position):
    return board[position]==" "

def full_board_check(board):
    for x in range(1,10):
        if space_check(board,x):
            return False
    return True

def player_choice(board):
    position=" "
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    play_again=input("Do you want to play again.Press 'Y' or 'N'").lower()
    if play_again=='y':
        clear()
        return True
    elif play_again=='n':
        return False
    else:
        print("wrong input")
        play_again=input("Do you want to play again.Press 'Y' or 'N'").lower()
    

#main logic
clear()
while True:
    # Reset the board
    print('Welcome to Tic Tac Toe!')

    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')
        
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn=='Player1':
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print("---------------------------------")
                print("  Congrats {} win  ".format(player1_marker))
                print("---------------------------------")
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player2'
        if turn=='Player2':
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
                
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print("---------------------------------")
                print("  Congrats {} win  ".format(player2_marker))
                print("---------------------------------")
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player1'
    if not replay():
        break
    



