import os
import time


from copy import deepcopy


def main():
    # input
    print(os.getcwd())
    day = "10"
    year = "2022"
    debug = True
    input_file = f'../inputs/day{day}{"_debug" if debug else ""}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()

    start_time = time.time()
    commands = []
    register_values = [1]
    for l in lines:
        if l[0] == 'n':
            commands.append((0, 0))
        else:
            commands.append((1, int(l.split(' ')[1])))

    # print(commands)
    for (c, arg) in commands:
        last_value = register_values[-1]
        register_values.append(last_value)
        if c != 0:
            register_values.append(last_value+arg)

    for i in range(20, len(register_values), 40):
        part1 += register_values[i-1] * i

    # part2
    display = [['.' for _ in range(40)] for _ in range(6)]

    for i in range(240):
        row, col = i//40, i % 40
        if (abs(col-register_values[i]) <= 1):
            display[row][col] = '#'
    output = '\n'.join([''.join(row) for row in display])
    print(output)

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 21
    print(
        f"{header}\n* AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")

    for r in register_values: print(r)
if __name__ == "__main__":
    main()
