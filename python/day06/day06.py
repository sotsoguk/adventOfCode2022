import os
import time
from string import ascii_lowercase
from collections import defaultdict
import timeit

inputt = ""


def first_all_unique(input, window_size=4):
    char_dict = {char: 0 for char in ascii_lowercase}
    for i, char in enumerate(input):
        char_dict[char] += 1
        if i >= window_size:
            char_dict[input[i-window_size]] -= 1
            # if all(v <= 1 for v in char_dict.values()):
            #     return i+1
            if any(v > 1 for v in char_dict.values()):
                continue
            else:
                return i+1

    # no position found
    return -1


def main():
    # input
    print(os.getcwd())
    day = "06"
    year = "2022"
    input_file = f'../inputs/day{day}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().split('\n\n')

    start_time = time.time()
    input = lines[0]
    inputt = lines[0]
    part1 = first_all_unique(input, window_size=4)
    for i in range(2000):
        part2 = first_all_unique(input, window_size=14)
    duration = int((time.time() - start_time) * 1000000)
    # benchmark
    stmt_code = "first_all_unique(inputt,14)"
    # setup_code = """
    # from __main__ import first_all_unique
    # from __main__ import input
    # """
    setup_code = """
from __main__ import first_all_unique
input = inputt
    """  # , input"
    # iterations = 10000
    # print(timeit.timeit(stmt=stmt_code,setup=setup_code,number= iterations,globals=globals())/iterations*1000000)
    header = "#" * 21
    print(
        f"{header}\n* AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
