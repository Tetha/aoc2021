
import sys
from dataclasses import dataclass

@dataclass
class Movement:
    horizontal_change: int = 0
    depth_change: int = 0

    def is_forward(self):
        return self.horizontal_change != 0

@dataclass
class Position:
    horizontal_position: int = 0
    depth: int = 0

    def move(self, movement: Movement):
        self.horizontal_position += movement.horizontal_change
        self.depth += movement.depth_change

@dataclass
class PositionWithAim:
    aim: int = 0
    horizontal_position: int = 0
    depth: int = 0

    def move(self, movement: Movement):
        if movement.is_forward():
            self.horizontal_position += movement.horizontal_change
            self.depth += movement.horizontal_change * self.aim
        else:
            self.aim += movement.depth_change

def main():
    if sys.argv[1] == "part1":
        part_1()
    elif sys.argv[1] == "part2":
        part_2()
    else:
        print("Arg required: part1/part2")

def part_1():
    data = open('input.txt', 'r').read().split('\n')
    parsed = parse_part_1(data)
    solve_part_1(parsed)

def part_2():
    data = open('input.txt', 'r').read().split('\n')
    parsed = parse_part_2(data)
    solve_part_2(parsed)

def parse_move(line):
    move, amount = line.split(' ')
    amount = int(amount)
    return {
        'forward': Movement(horizontal_change=amount),
        'down': Movement(depth_change=amount),
        'up': Movement(depth_change=-amount)
    }[move]

def parse_part_1(lines) -> list[Movement]:
    return map(parse_move, filter(lambda l: l != "", lines))

def solve_part_1(moves: list[Movement]):
    position = Position()
    for move in moves:
        position.move(move)
    print(position.horizontal_position * position.depth)

def parse_part_2(lines):
    return parse_part_1(lines)

def solve_part_2(moves: list[Movement]):
    position = PositionWithAim()
    for move in moves:
        print(f"position=#{position} // move=#{move}")
        position.move(move)
    print(position.horizontal_position * position.depth)
    pass

if __name__ == "__main__":
    main()