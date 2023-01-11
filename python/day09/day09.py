import os
import time
import cmath
import numpy as np
from copy import deepcopy


def abs_l1(x, y):
    return int(max(
        abs(x.real-y.real),
        abs(x.imag - y.imag)))


def touching(x, y):
    return abs_l1(x, y) <= 1


def touching2(x, y):
    return (abs(x.real-y.real) + abs(x.imag-y.imag)) <= 10


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def calc_part1(commands):
    visited_pos = set()
    head, tail = complex(0, 0), complex(0, 0)
    visited_pos.add(tail)
    phase_dict = {0: complex(1, 1), 1: complex(-1, 1),
                  2: complex(-1, -1), 3: complex(1, -1)}
    for c in commands:
        head += c

        if not touching(head, tail):
            hx, hy = head.real, head.imag
            tx, ty = tail.real, tail.imag
            if hx == tx:
                tail += complex(0, 1) * sign(hy-ty)
            elif hy == ty:
                tail += complex(1, 0) * sign(hx-tx)
            else:
                p = (int(np.degrees(cmath.phase(head-tail))) % 360) // 90
                tail += phase_dict[p]
        visited_pos.add(tail)
    return len(visited_pos)

def calc_part2(commands):
    visited_pos = set()
    head, tail = complex(0, 0), complex(0, 0)
    visited_pos.add(tail)
    phase_dict = {0: complex(1, 1), 1: complex(-1, 1),
                  2: complex(-1, -1), 3: complex(1, -1)}
    debug_pos = []
    for c in commands:
        head += c

        if not touching2(head, tail):
            hx, hy = head.real, head.imag
            tx, ty = tail.real, tail.imag
            if hx == tx:
                tail += complex(0, 1) * sign(hy-ty)
            elif hy == ty:
                tail += complex(1, 0) * sign(hx-tx)
            else:
                p = (int(np.degrees(cmath.phase(head-tail))) % 360) // 90
                tail += phase_dict[p]
        visited_pos.add(tail)
        debug_pos.append(tail)
        # debug output
    # min_x,min_y = 100,100
    # max_x,max_y = -100,-100
    # for p in debug_pos:
    #     px = int(p.real)
    #     py = int(p.imag)
    #     min_x = min(min_x,px)
    #     max_x = max(max_x,px)
    #     min_y = min(min_y,py)
    #     max_y = max(max_y,py)
    # print(min_x,min_y,max_x,max_y)
    # grid = [['.' for _ in range (max_x-min_x+1)] for _ in range(max_y-min_y+1)]
    # for p in debug_pos:
    #     print(int(p.real),int(p.imag))
    #     grid[max_y-(int(p.imag))][int(p.real)-min_x] = '#'
    # #output = '\n'.join([''.join(row) for row in display])
    # output = '\n'.join([''.join(row) for row in grid])
    # print(output)
    return len(visited_pos)
def main():
    # input
    print(os.getcwd())
    day = "09"
    year = "2022"
    debug = False
    input_file = f'../inputs/day{day}{"_debug" if debug else ""}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()
    start_time = time.time()

    commands = []
    head_dict = {'R': complex(1, 0), 'U': complex(
        0, 1), 'L': complex(-1, 0), 'D': complex(0, -1)}
    for l in lines:
        direction, steps = l.split(' ')
        commands.append((head_dict[direction], int(steps)))
    commands_unpacked = []
    for (d, s) in commands:
        for i in range(s):
            commands_unpacked.append(d)

    # print(commands)
    # print(commands_unpacked)

    # part1

    # output
    # print(visited_pos)
    # part1 = calc_part1(commands_unpacked)
    part2 = calc_part2(commands_unpacked)
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 21
    print(
        f"{header}\n* AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
