
from collections import defaultdict
import sys
from typing import Dict, Tuple

from day5.line_segment import parse_line_segment_line

def main(args):
    print(args)
    if args[1] == "test":
        test_part_1()
    elif args[1] == "part1":
        part_1()
    elif args[1] == "part2":
        part_2()
    else:
        print("Arg required: part1/part2")

def test_part_1():
    data = open('day5/test_input.txt', 'r').read().split('\n')
    data = list(filter(lambda l: l != "", data))
    parsed = parse_part_1(data)
    solve_part_1(parsed)

def part_1():
    data = open('day5/input.txt', 'r').read().split('\n')
    data = list(filter(lambda l: l != "", data))
    parsed = parse_part_1(data)
    solve_part_1(parsed)

def part_2():
    data = open('day5/input.txt', 'r').read().split('\n')
    data = list(filter(lambda l: l != "", data))
    parsed = parse_part_2(data)
    solve_part_2(parsed)

def parse_part_1(lines):
    segments = [parse_line_segment_line(l) for l in lines]
    return segments

def solve_part_1(segments):
    grid_locations: Dict[Tuple[int, int], int] = defaultdict(int)

    for segment in segments:
        if segment.x1 == segment.x2:
            print("x same: ", segment)
            for y in range(min(segment.y1, segment.y2), max(segment.y1, segment.y2)+1):
                grid_locations[(segment.x1, y)] += 1
            continue

        if segment.y1 == segment.y2:
            print("y same: ", segment)
            for x in range(min(segment.x1, segment.x2), max(segment.x1, segment.x2)+1):
                grid_locations[(x, segment.y1)] += 1
            continue

        print("none same", segment)
        line_length = abs(segment.x1-segment.x2)+1
        step_x = 1 if segment.x2-segment.x1 > 0 else -1
        step_y = 1 if segment.y2-segment.y1 > 0 else -1
        for i in range(line_length):
            new_x = segment.x1 + i*step_x
            new_y = segment.y1 + i*step_y
            grid_locations[(new_y, new_x)] += 1
    print(len(list(1 for segments in grid_locations.values() if segments >= 2)))

def parse_part_2(lines):
    return parse_part_1(lines)

def solve_part_2(data):
    pass

if __name__ == "__main__":
    main(sys.argv)