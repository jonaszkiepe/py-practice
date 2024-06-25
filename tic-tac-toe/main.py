import os

positions = [["123", "456", "789"],
             ["147", "258", "369"],
             ["159", "357"]]


def check_win(player):
    for position in positions:
        for chars in position:
            if "xxx" in chars or "ooo" in chars:
                print(f"player {player} won!")
                return True


def gen_board():
    os.system("clear")
    board = ""
    for row in positions[0]:
        for char in row:
            if char not in "xo": board += " |"
            else: board += char + "|"
        board = board[:-1] + "/-----/"
    for row in board.split("/")[:-2]: print(row)


def replace_number(replace, player):
    if player == 1: symbol = "x"
    elif player == 2: symbol = "o"
    for k in range(len(positions)):
        for j in range(len(positions[k])):
            positions[k][j] = positions[k][j].replace(replace, symbol)


def main():
    switch, player = 1, 1
    for i in range(0, 9):
        gen_board()
        if check_win(player): return
        replace_number(input(f"Player {player} turn: "), player)
        switch, player = switch * -1, player + switch
    gen_board()
    print("Draw")


if __name__ == "__main__":
    main()
