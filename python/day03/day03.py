import os
import time
from string import ascii_lowercase, ascii_uppercase


def calc_priority(character):
    if character in ascii_lowercase:
        return (ord(character)-96)
    elif character in ascii_uppercase:
        return (ord(character)-38)


def solve_part1(rucksack):
    rucksack_sets = map(
        set, [rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]])
    return calc_priority(set.intersection(*rucksack_sets).pop())


def solve_part2(rucksacks):
    score = 0
    for i in range(0, len(rucksacks), 3):
        rucksack_sets = map(set, [l for l in rucksacks[i:i+3]])
        score += (calc_priority(set.intersection(*rucksack_sets).pop()))
    return score


def main():
    # input
    print(os.getcwd())
    day = "03"
    year = "2022"
    input_file = f'../inputs/day{day}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()

    start_time = time.time()
    # part 1
    for l in lines:
        part1 += solve_part1(l)

    # part 2
    part2 = solve_part2(lines)

    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
