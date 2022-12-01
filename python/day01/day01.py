import os
import time


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
    curr_calories = []
    for l in lines:
        if l == "":
            calories.append(curr_calories.copy())
            curr_calories = []
        else:
            curr_calories.append(int(l, base=10))
    calories.append(curr_calories)

    start_time = time.time()

    # part1 & 2
    total_cals = [sum(c) for c in calories]

    part1 = max(total_cals)
    part2 = sum(sorted(total_cals)[-3:])

    duration = int((time.time() - start_time) * 1000000)

    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
