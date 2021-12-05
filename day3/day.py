
import sys
from typing import Tuple, get_origin

def main():
    if sys.argv[1] == "test":
        test()
    elif sys.argv[1] == "part1":
        part_1()
    elif sys.argv[1] == "part2":
        part_2()
    else:
        print("Arg required: part1/part2")

def test():
    data = open('test_input.txt', 'r').read().split('\n')
    data = list(filter(lambda l: l != "", data))
    parsed = parse_part_1(data)
    print(solve_part_1(parsed))

def part_1():
    data = open('input.txt', 'r').read().split('\n')
    data = list(filter(lambda l: l != "", data))
    parsed = parse_part_1(data)
    print(solve_part_1(parsed))

def part_2():
    data = open('input.txt', 'r').read().split('\n')
    data = list(filter(lambda l: l != "", data))
    parsed = parse_part_2(data)
    solve_part_2(parsed)

def parse_part_1(lines):
    return lines

def get_most_common_bit(bitstrings: list[str], index: int) -> Tuple[int, bool]:
    """
    >>> get_most_common_bit(['10110', '10111'], 4)
    (1, True)
    """
    ones = 0
    zeroes = 0
    for bitstring in bitstrings:
        bit = bitstring[index]
        if bit == "1":
            ones += 1
        else:
            zeroes += 1
    if ones == zeroes:
        return 1, True
    elif ones > zeroes:
        return 1, False
    else:
        return 0, False

def solve_part_1(data) -> int:
    """
    >>> solve_part_1([
    ... "00100",
    ... "11110",
    ... "10110",
    ... "10111",
    ... "10101",
    ... "01111",
    ... "00111",
    ... "11100",
    ... "10000",
    ... "11001",
    ... "00010",
    ... "01010",
    ... ])
    198
    """
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(data[0])):
        most_common, was_equal = get_most_common_bit(data, i)
        if most_common == 1:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    gamma_rate_int = int(gamma_rate, 2)
    epsilon_rate_int = int(epsilon_rate, 2)

    return gamma_rate_int * epsilon_rate_int


def parse_part_2(lines):
    return parse_part_1(lines)

def do_bit_selection(data, use_most_common_bit, equal_bit) -> int:
    """
    >>> do_bit_selection([
    ...   "00100",
    ...   "11110",
    ...   "10110",
    ...   "10111",
    ...   "10101",
    ...   "01111",
    ...   "00111",
    ...   "11100",
    ...   "10000",
    ...   "11001",
    ...   "00010",
    ...   "01010",
    ... ], True, 1)
    23
    >>> do_bit_selection([
    ...   "00100",
    ...   "11110",
    ...   "10110",
    ...   "10111",
    ...   "10101",
    ...   "01111",
    ...   "00111",
    ...   "11100",
    ...   "10000",
    ...   "11001",
    ...   "00010",
    ...   "01010",
    ... ], False, 0)
    10
    """
    work_data = list(data) # don't mutate inputs
    i = 0

    while len(work_data) > 1:
        most_common, was_equal = get_most_common_bit(work_data, i)
        if was_equal:
            most_common = str(equal_bit)
        elif use_most_common_bit:
            most_common = str(most_common)
        else:
            most_common = str(1 - most_common)
        work_data = [bs for bs in work_data if bs[i] == most_common]
        i += 1
    
    return int(work_data[0], 2)

def solve_part_2(data):
    oxygen_rating = do_bit_selection(data, True, 1) 
    scrubber_rating = do_bit_selection(data, False, 0)
    print(oxygen_rating, scrubber_rating, oxygen_rating * scrubber_rating)

if __name__ == "__main__":
    main()