import os
import random


def clear():
    os.system("clear")


positions = [["123", "456", "789"],
             ["147", "258", "369"],
             ["159", "357"]]


def check_win():
    for position in positions:
        for chars in position:
            if "xxx" in chars or "ooo" in chars:
                return True


def gen_board():
    board = ""
    for row in positions[0]:
        for char in row:
            board += char + "|"
        board = board[:-1]
        board += " "
    for row in board.split():
        print(row)


def replace_number(replace, player):
    if player == 1:
        symbol = "x"
    if player == 2:
        symbol = "o"
    for position in positions:
        for chars in position:
            index1 = positions.index(position)
            index2 = position.index(chars)
            positions[index1][index2] = chars.replace(replace, symbol)


def switch_player(player):
    if player == 1:
        return 2
    if player == 2:
        return 1


def main():
    clear()
    player = random.randint(1, 2)
    while True:
        print(f"player {player} turn")
        gen_board()
        replace_number(input(), player)
        if check_win():
            break
        player = switch_player(player)
        clear()
    clear()
    gen_board()
    print(f"player {player} won!")


if __name__ == "__main__":
    main()
