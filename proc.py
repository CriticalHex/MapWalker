import numpy
import random
import os


def pick_direction(x: int, y: int) -> tuple[int, int]:
    r = random.randint(1, 4)
    if r == 1:
        return x, y - 1
    if r == 2:
        return x + 1, y
    if r == 3:
        return x, y + 1
    return x - 1, y


def off_side(board: list[list[str]], x: int, y: int):
    if not (0 <= x < len(board[0])):
        return True
    if not (0 <= y < len(board)):
        return True
    return False


def surrounded(board: list[list[str]], x: int, y: int):
    return (off_side(board, x, y - 1) or board[y - 1][x] != " ") and\
        (off_side(board, x + 1, y) or board[y][x + 1] != " ") and\
        (off_side(board, x, y + 1) or board[y + 1][x] != " ") and\
        (off_side(board, x - 1, y) or board[y][x - 1] != " ")


def propagate(board: list[list[str]], x: int, y: int):
    ox, oy = x, y
    chosen_x, chosen_y = x, y
    while not surrounded(board, chosen_x, chosen_y):
        while off_side(board, chosen_x, chosen_y) or board[chosen_y][chosen_x] != " ":
            chosen_x, chosen_y = pick_direction(ox, oy)
        ox, oy = chosen_x, chosen_y
        board[chosen_y][chosen_x] = str(random.randint(2, 5))
        print_board(board)


def print_board(board: list[list[str]]):
    os.system("cls")
    print(numpy.matrix(board))


def main():
    board: list[list[str]] = [[" " for _ in range(10)] for _ in range(10)]
    start_x, start_y = random.randint(0, 9), random.randint(0, 9)
    board[start_y][start_x] = "1"
    propagate(board, start_x, start_y)


main()
