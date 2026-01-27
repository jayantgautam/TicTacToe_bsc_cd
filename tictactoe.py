
name = input("Your good name ")
print("hi", name)
name2 = input("2nd player name: ")
print("So,", str.upper(name), "you can start the game and you will be the 'X' and", str.upper(name2), "will get the 'O' or u can do viceversa")
file = open("gamerule.txt", "r")
content = file.read()
print(content)
file.close()
input("press enter to start the game")

#board range
board = [' ' for _ in range(9)]

#player symbols
player_symbols = ['X', 'O']

#for printing game board
def print_board():
    for i in range(0, 9, 3):
        print(f' {board[i]} | {board[i+1]} | {board[i+2]} ')
        if i < 6:
            print('-----------')

#if player win
def check_win(player):
    #check rows
    for i in range(0, 9, 3):
        if board[i] == player and board[i+1] == player and board[i+2] == player:
            return True

    #check columns
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True

    #check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    elif board[2] == board[4] == board[6] == player:
        return True
    return False

#if game drow
def check_draw():
    return ' ' not in board

#the game loop
current_player = 0
while True:
    print_board()
    player = player_symbols[current_player]
    position = int(input(f"Player {player}, enter a position (1-9): ")) - 1

    if board[position] == ' ':
        board[position] = player

        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            break

        elif check_draw():
            print_board()
            print("It's a draw!")
            break
        current_player = (current_player + 1) % 2

    else:
        print("That position is already taken. Try again.")

#winners record
with open("game history.txt", 'a') as file:
    file.write("\n" + str(name) + " and " + str(name2) + " were playing and player carrying '" + str(player) + "' win")



