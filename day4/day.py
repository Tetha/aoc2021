
import sys
from typing import Tuple

from .bingo_board import BingoBoard

def main():
    if sys.argv[1] == "test":
        part_test()
    elif sys.argv[1] == "part1":
        part_1()
    elif sys.argv[1] == "part2":
        part_2()
    else:
        print("Arg required: part1/part2")

def part_test():
    data = open('input_test.txt', 'r').read().split('\n')
    data = list(filter(lambda l: l != "", data))
    parsed = parse_part_1(data)
    solve_part_1(parsed)

def part_1():
    data = open('input.txt', 'r').read().split('\n')
    data = list(filter(lambda l: l != "", data))
    parsed = parse_part_1(data)
    solve_part_1(parsed)

def part_2():
    data = open('input.txt', 'r').read().split('\n')
    data = list(filter(lambda l: l != "", data))
    parsed = parse_part_2(data)
    solve_part_2(parsed)

def parse_part_1(lines):
    number_line = lines[0]
    lines = lines[1:]

    numbers = number_line.split(',')

    boards = []
    while lines:
        board = lines[:5]
        lines = lines[5:] # following empty line
        print(board)
        boards.append(BingoBoard.from_lines(5, board))

    return (numbers, boards)

def solve_part_1(data: Tuple[list[str], list[BingoBoard]]):
    numbers, boards = data

    for number in numbers:
        # mark on all boards
        for board in boards:
            board.mark_number(number)

        for board in boards:
            if board.is_won():
                print(int(number) * board.score())
                return


def parse_part_2(lines):
    return parse_part_1(lines)

def solve_part_2(data: Tuple[list[str], list[BingoBoard]]):
    numbers, boards = data

    for number in numbers:
        # mark on all boards
        for board in boards:
            board.mark_number(number)

        for board in boards:
            if board.is_won():
                if len(boards) == 1: # last one
                    print(int(number) * boards[0].score())
                    return
                else:
                    boards.remove(board)

    pass

if __name__ == "__main__":
    main()