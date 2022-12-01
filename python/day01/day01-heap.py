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
        lines = f.read().splitlines()

    # parse input
    calories = []
    curr_calories = 0
    for l in lines:
        if l == "":
            calories.append(curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(l, base=10)
    calories.append(curr_calories)

    start_time = time.time()

    # part1 & 2
    heapq.heapify(calories)

    part1 = max(calories)
    part2 = sum(heapq.nlargest(3, calories))

    duration = int((time.time() - start_time) * 1000000)

    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
