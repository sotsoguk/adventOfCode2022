import os
import time
import re


def main():
    # input
    print(os.getcwd())
    day = "04"
    year = "2022"
    input_file = f'../inputs/day{day}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()

    start_time = time.time()

    rgs = [list(map(int, re.split('-|,', l))) for l in lines]

    def contains(r): return (r[0] >= r[2] and r[1] <= r[3]) or (
        r[2] >= r[0] and r[3] <= r[1])

    def overlap(r): return not(r[1] < r[2] or r[3] < r[0])
    part1 = sum(map(contains, rgs))
    part2 = sum(map(overlap, rgs))

    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 21
    print(
        f"{header}\n* AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
