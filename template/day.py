
import sys

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

def parse_part_1(lines):
    pass

def solve_part_1(data):
    pass

def parse_part_2(lines):
    return parse_part_1(lines)

def solve_part_2(data):
    pass

if __name__ == "__main__":
    main()