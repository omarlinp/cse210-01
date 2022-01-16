

from multiprocessing.sharedctypes import Value
from optparse import Values
from random import choice


def main():
    player_1 = input('Enter your name:')
    player_2 = input('Enter your name:')

    cur_player = player_1

    player_choice = {'X' : "", 'O' : ""}

    options = ['X', 'O']

    while True:
        print("Turn to choose for", cur_player)

        try:
            choice = int(input('Enter 1 for X\nEnter 2 for O\nEnter 3 to quit the game'))
        except ValueError:
            print('Wrong input. please try again')
            continue
        
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player_1:
                player_choice['O'] = player_2
            else:
                player_choice['O'] = player_1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player_1:
                player_choice['X'] = player_2
            else:
                player_choice['X'] = player_1
        elif choice == 3:
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
        winner = game(options[choice-1])

#function to print the board
def display_board(values):
    print("\n")
    print("\t     |     |")
    print(f"\t  {values[0]}  |  {values[1]}  |  {values[2]}")
    print("\t_____|_____|_____")

    print("\t     |     |")
    print(f"\t  {values[3]}  |  {values[4]}  |  {values[5]}")
    print("\t_____|_____|_____")

    print("\t     |     |")

    print("\t     |     |")
    print(f"\t  {values[6]}  |  {values[7]}  |  {values[8]}")
    print("\t_____|_____|_____")
def check_for_win(player_pos,cur_player):

    combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    for x in combinations:
        if all(y in player_pos[cur_player] for y in x):

            return True
    return False
def check_for_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False

def game(cur_player):

    values = [' ' for x in range(9)]

    player_pos = {'X':[], 'O':[]}
    while True:
        display_board(values)
        try:
            move = int(input('select a box:'))
            
        except  ValueError:
            print('Wrong choice, try again')
            continue
        if move < 1 or move > 9:
            print('Wrong choice, try again')
            continue
        if values[move-1] != ' ':
            print('Place is already filled. Try again')
            continue

        values[move-1] = cur_player
        
        player_pos[cur_player].append(move)

        if check_for_win(player_pos,cur_player):
            display_board(values)
            print(f'Player {cur_player} has won!!')
            return cur_player

        if check_for_draw(player_pos):
            display_board(values)
            print('Game Drawn')
            return 'D'
        if cur_player == 'X':
            cur_player='O'
        else:
            cur_player = 'X'
if __name__ == "__main__":
    main()