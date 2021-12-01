
import sys
from typing import List

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

def parse_part_1(lines: str) -> List[int]:
    return [int(l) for l in lines if l != ""]

def solve_part_1(data: List[int]):
    pairs = zip(data, data[1:])
    increasing_pairs = [p for p in pairs if p[0] < p[1]]
    print(len(increasing_pairs))

def parse_part_2(lines: str):
    return parse_part_1(lines)

def solve_part_2(data):
    windows = zip(data, data[1:], data[2:])
    sums = [sum(w) for w in windows]
    solve_part_1(sums)

if __name__ == "__main__":
    main()