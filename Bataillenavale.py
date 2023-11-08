from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row) #Décomenter si vous voulez la position des bateaux
#print(ship_col)

for turn in range(4):
    print("Tour", turn + 1)
    guess_row = int(input("Ligne:"))
    guess_col = int(input("Colonne:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Félicitations! Vous avez coulé mon navire!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oups, cette case n'est pas dans l'océan.")
        elif(board[guess_row][guess_col] == "X"):
            print("Vous avez déjà tiré sur cette case.")
        else:
            print("Vous avez manqué mon navire!")
            board[guess_row][guess_col] = "X"
        if (turn == 3):
            print("Game Over")
        print_board(board)
