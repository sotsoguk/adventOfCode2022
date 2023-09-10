import os
import time
import heapq

def main():

    # input
    print(os.getcwd())
    day = "01"
    year = "2022"
    input_file = f'../inputs/day{day}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        groups = f.read().split('\n\n')

    start_time = time.time()
    # calc
    calories = sorted([sum(list(map(int, group.splitlines())))
                      for group in groups])
    part1 = calories[-1]
    part2 = sum(calories[-3:])

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
